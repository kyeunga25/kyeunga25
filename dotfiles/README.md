# Dotfiles

These files are a portable, public-safe subset of the configuration used on macOS.
Machine-specific paths, credentials, history, caches, sessions, and private keys are intentionally excluded.

## Install

Install Homebrew packages from the repository root:

    brew bundle

Back up any existing files, then link the tracked configuration:

    ln -s "$PWD/dotfiles/zsh/.zshrc" "$HOME/.zshrc"
    ln -s "$PWD/dotfiles/zsh/.zprofile" "$HOME/.zprofile"
    ln -s "$PWD/dotfiles/zsh/.p10k.zsh" "$HOME/.p10k.zsh"
    ln -s "$PWD/dotfiles/tmux/.tmux.conf" "$HOME/.tmux.conf"

The Zsh config works with or without Oh My Zsh. Optional aliases and completions are guarded so missing tools do not prevent the shell from starting.
