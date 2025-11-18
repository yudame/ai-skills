#!/bin/zsh

# Claude Code MCP Selector
# Add this to your ~/.zshrc

cc() {
  local user_dir="$HOME/.claude/mcp-available"
  local project_dir="./mcp-available"
  local output_file="$HOME/.claude/mcp.json"
  local project_override="./.mcp.json"

  # Ensure user directory exists
  mkdir -p "$user_dir"

  # Arrays to store available MCPs
  local -a user_mcps
  local -a project_mcps
  local -A mcp_files  # Map option number to file path
  local -A mcp_sources # Map option number to source (user/project)

  # Scan user MCPs
  if [[ -d "$user_dir" ]]; then
    for file in "$user_dir"/*.json(N); do
      if [[ -f "$file" ]]; then
        local name="${file:t:r}"  # Get filename without path and extension
        user_mcps+=("$name")
      fi
    done
  fi

  # Scan project MCPs
  if [[ -d "$project_dir" ]]; then
    for file in "$project_dir"/*.json(N); do
      if [[ -f "$file" ]]; then
        local name="${file:t:r}"
        project_mcps+=("$name")
      fi
    done
  fi

  # Build option mapping
  local counter=1
  for name in "${user_mcps[@]}"; do
    mcp_files[$counter]="$user_dir/$name.json"
    mcp_sources[$counter]="user"
    ((counter++))
  done

  for name in "${project_mcps[@]}"; do
    mcp_files[$counter]="$project_dir/$name.json"
    mcp_sources[$counter]="project"
    ((counter++))
  done

  # Display menu
  echo
  echo "╭─────────────────────────────╮"
  echo "│     Claude Code MCPs        │"
  echo "╰─────────────────────────────╯"
  echo
  echo "  e) empty (no MCPs)"
  echo "  a) all"
  echo "  n) require permissions (default: skip)"
  echo

  if [[ ${#user_mcps[@]} -gt 0 ]]; then
    echo "User:"
    local i=1
    for name in "${user_mcps[@]}"; do
      printf "  %2d) %s\n" $i "$name"
      ((i++))
    done
    echo
  fi

  if [[ ${#project_mcps[@]} -gt 0 ]]; then
    echo "Project:"
    local start=$((${#user_mcps[@]} + 1))
    local i=$start
    for name in "${project_mcps[@]}"; do
      printf "  %2d) %s\n" $i "$name"
      ((i++))
    done
    echo
  fi

  echo "────────────────────────────────"
  echo -n "Select (space-separated): "
  read -r selection
  echo

  # Parse selection for 'n' flag and filter it out
  local skip_permissions=true
  local filtered_selection=""

  for item in ${=selection}; do
    if [[ "$item" == "n" ]]; then
      skip_permissions=false
    else
      filtered_selection="$filtered_selection $item"
    fi
  done

  # Trim leading space
  filtered_selection="${filtered_selection## }"

  # Build claude command args
  local -a claude_args
  if [[ "$skip_permissions" == "true" ]]; then
    claude_args+=(--dangerously-skip-permissions)
  fi
  claude_args+=("$@")

  # Process selection
  local -a selected_files
  local -a selected_names

  if [[ "$filtered_selection" == "e" ]]; then
    # Empty mode - no MCPs
    echo '{"mcpServers":{}}' > "$output_file"
    echo '{"mcpServers":{}}' > "$project_override"
    echo "→ Running empty (no MCPs)"
    if [[ "$skip_permissions" == "true" ]]; then
      echo "→ Skipping permissions"
    else
      echo "→ Requiring permissions"
    fi
    echo
    claude "${claude_args[@]}"
    return
  elif [[ "$filtered_selection" == "a" ]]; then
    # All mode - select everything (project overrides user)
    for num in ${(k)mcp_files}; do
      selected_files+=("${mcp_files[$num]}")
      local name="${mcp_files[$num]:t:r}"
      selected_names+=("$name")
    done
  else
    # Parse space-separated numbers
    for num in ${=filtered_selection}; do
      if [[ -n "${mcp_files[$num]}" ]]; then
        selected_files+=("${mcp_files[$num]}")
        local name="${mcp_files[$num]:t:r}"
        selected_names+=("$name")
      fi
    done
  fi

  if [[ ${#selected_files[@]} -eq 0 ]]; then
    echo "No valid selection. Running empty."
    echo '{"mcpServers":{}}' > "$output_file"
    echo '{"mcpServers":{}}' > "$project_override"
    if [[ "$skip_permissions" == "true" ]]; then
      echo "→ Skipping permissions"
    else
      echo "→ Requiring permissions"
    fi
    echo
    claude "${claude_args[@]}"
    return
  fi

  # Merge selected configs
  # Start with empty mcpServers object
  local merged='{"mcpServers":{}}'

  for file in "${selected_files[@]}"; do
    if [[ -f "$file" ]]; then
      # Read the config object and merge into mcpServers
      local config=$(cat "$file")
      merged=$(echo "$merged" | jq --argjson new "$config" '.mcpServers += $new')
    fi
  done

  # Write merged config
  echo "$merged" | jq '.' > "$output_file"

  # Write empty project override to block parent configs
  echo '{"mcpServers":{}}' > "$project_override"

  # Display what we're loading
  echo -n "→ Loading: "
  echo "${selected_names[@]}"
  if [[ "$skip_permissions" == "true" ]]; then
    echo "→ Skipping permissions"
  else
    echo "→ Requiring permissions"
  fi
  echo

  # Launch Claude Code
  claude "${claude_args[@]}"
}
