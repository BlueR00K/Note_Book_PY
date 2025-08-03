# Summary: Generating a New SSH Key and Adding It to the SSH Agent (GitHub)

This guide covers how to generate a new SSH key for GitHub authentication and add it to the SSH agent.

## About SSH Key Passphrases

- SSH keys allow secure authentication to GitHub.
- You can add a passphrase for extra security; the SSH agent can remember your passphrase.

## Checking for Existing SSH Keys

- Before generating a new key, check if you already have one.
- See: [Checking for existing SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)

### Practical: How to Check for Existing SSH Keys in Windows

1. **Open PowerShell or Command Prompt.**
2. **Navigate to your SSH directory:**

   ```powershell
   cd $env:USERPROFILE\.ssh
   ```

## Generating a New SSH Key

- Recommended: Ed25519 algorithm

  ```
  ssh-keygen -t ed25519 -C "your_email@example.com"
  ```

- For legacy systems: RSA algorithm

  ```
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```

- Accept the default file location or specify a custom name.
- Enter a secure passphrase (optional).

## Adding Your SSH Key to the SSH Agent

- Start the ssh-agent:

  - **Windows PowerShell:**

    ```powershell
    Get-Service -Name ssh-agent | Set-Service -StartupType Manual
    Start-Service ssh-agent
    ssh-add $env:USERPROFILE\.ssh\id_ed25519
    ```

  - **macOS/Linux:**

    ```sh
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```

- For macOS, you may need to update your `~/.ssh/config` to automatically load keys and store passphrases in your keychain.

## Adding the SSH Key to Your GitHub Account

- Copy your public key (e.g., `id_ed25519.pub`).
- Go to [GitHub SSH keys settings](https://github.com/settings/keys).
- Click "New SSH key", paste your key, and save.

## Generating a New SSH Key for a Hardware Security Key

- Use `ssh-keygen -t ed25519-sk -C "your_email@example.com"` for supported hardware keys.
- If unsupported, use `ssh-keygen -t ecdsa-sk -C "your_email@example.com"`.

### Practical: Copy SSH Public Key to Clipboard in Windows CMD

To copy the contents of your public key (e.g., `id_rsa.pub`) to the clipboard, run:

```cmd
type %USERPROFILE%\.ssh\id_rsa.pub | clip
```

## Additional Resources

- [About SSH key passphrases](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#about-ssh-key-passphrases)
- [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
- [Troubleshooting SSH](https://docs.github.com/en/authentication/troubleshooting-ssh)

---
This summary is based on [GitHub Docs: Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
