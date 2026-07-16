# Powerlevel10k instant prompt should stay near the top of this file.
if [[ -r "\${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-\${(%):-%n}.zsh" ]]; then
  source "\${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-\${(%):-%n}.zsh"
fi

export ZSH="\${ZSH:-$HOME/.oh-my-zsh}"

# Use the Oh My Zsh copy when present. Homebrew's copy is loaded below.
if [[ -r "$ZSH/custom/themes/powerlevel10k/powerlevel10k.zsh-theme" ]]; then
  ZSH_THEME="powerlevel10k/powerlevel10k"
else
  ZSH_THEME=""
fi

plugins=(
  git
  docker
  kubectl
)

[[ -r "$ZSH/oh-my-zsh.sh" ]] && source "$ZSH/oh-my-zsh.sh"

# Homebrew formulae installed by the Brewfile.
if [[ -n "\${HOMEBREW_PREFIX:-}" ]]; then
  [[ -r "$HOMEBREW_PREFIX/share/powerlevel10k/powerlevel10k.zsh-theme" && -z "$ZSH_THEME" ]] && \
    source "$HOMEBREW_PREFIX/share/powerlevel10k/powerlevel10k.zsh-theme"
  [[ -r "$HOMEBREW_PREFIX/share/zsh-autosuggestions/zsh-autosuggestions.zsh" ]] && \
    source "$HOMEBREW_PREFIX/share/zsh-autosuggestions/zsh-autosuggestions.zsh"
  [[ -r "$HOMEBREW_PREFIX/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" ]] && \
    source "$HOMEBREW_PREFIX/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
  [[ -r "$HOMEBREW_PREFIX/etc/profile.d/autojump.sh" ]] && \
    source "$HOMEBREW_PREFIX/etc/profile.d/autojump.sh"
  [[ -d "$HOMEBREW_PREFIX/opt/ruby/bin" ]] && path=("$HOMEBREW_PREFIX/opt/ruby/bin" $path)
fi

# Keep colorls optional so a missing Ruby gem never breaks shell startup.
if (( $+commands[colorls] )); then
  alias ls='colorls --group-directories-first'
  alias ll='colorls -lA --sd --gs --group-directories-first'
  alias l='colorls -l --sort-dirs'
  alias la='colorls -la --sort-dirs'
  alias lt='colorls -lt --git-status'
  alias lS='colorls -lS --git-status'
  alias lr='colorls --tree=5'
  alias lx='colorls -lAX --git-status'
else
  alias ll='ls -lA'
  alias la='ls -la'
fi

[[ -r "$HOME/.fzf.zsh" ]] && source "$HOME/.fzf.zsh"

if (( $+commands[kubectl] )); then
  source <(kubectl completion zsh)
  alias k=kubectl
  (( $+functions[compdef] )) && compdef k=kubectl
fi

[[ -r "$HOME/.p10k.zsh" ]] && source "$HOME/.p10k.zsh"
[[ -r "$HOME/.local/bin/env" ]] && source "$HOME/.local/bin/env"
