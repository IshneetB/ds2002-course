# Setting Up

## Git & GitHub (Required)

Everyone will need a GitHub account. If you already have a GitHub account, you can skip step 1. 

### Step 1: Create a GitHub Account

1. Go to [github.com](https://github.com) and click **Sign up**
2. Follow the prompts to create your account
3. Verify your email address if required

### Step 2: Fork the Repository

1. Navigate to the original repository on GitHub
2. Click the **Fork** button in the top-right corner
3. Select your account as the destination for the fork, e.g. if your GitHub account is "msmith", you'd use `msmith/ds2002-course` as the name for the forked repo (should be set as default).
4. Wait for the fork to complete
5. Bookmark the webpage of your forked GitHub repository. You will be using it frequently :) 

### Step 3: Create a Personal Access Token (PAT)

**Note:** This step is required if you plan to use git on your own computer/laptop.

Personal Access Tokens (PATs) are an established best practice for securing access to your repositories. Unlike SSH keys, which grant broad access, PATs provide more granular control over what actions are allowed. You can create tokens with specific scopes (like read-only access, or access only to certain repositories), making them more secure and easier to manage. PATs are also easier to revoke if compromised, as you can delete individual tokens without affecting your entire account.

1. Go to GitHub Settings → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Click **Generate new token** → **Generate new token (classic)**
3. Give your token a descriptive name (e.g., "DS2002 Course")
4. Select the **repo** scope (this enables clone, pull, push, and submitting pull requests)
5. Set the token expiration date to May 31, 2026.
6. Click **Generate token** at the bottom
7. **Copy the token immediately** - you won't be able to see it again!
8. Store it securely (you'll use it as your password when using git from your local machine)

## Using GitHub Codespaces for Your Projects (Recommended)

The easiest way to get started is to use GitHub Codespaces. You can launch Codespaces directly through your repo in GitHub; all the software tools you will need are already configured and will be at your disposal with a single click of a button. It couldn't be easier. 

1. In your forked repository, click the green **Code** button
2. Select the **Codespaces** tab
3. Click **Create codespace on main** (or select a branch)
4. GitHub will automatically detect and use the default devcontainer configuration
5. Wait for the codespace to initialize (this may take a few minutes)

You should see a screen like this:
![Screenshot of terminal in GitHub Codespaces](/docs/images/codespaces.png)

Once your codespace is ready, you'll have a fully configured development environment in your browser!

## Setting Up Your Own Computer for Course Projects (Optional)

**Note: If you are new to programming and are not familiar with installing programming tools on your computer, I highly recommend skipping this step and using GitHub Codespaces instead.** This will allow you to get started immediately without the hassle of troubleshooting any setup issues.

However, if you want to set up an environment for class work on your own computer, here are the basic steps. 

To set up your own computer for all course activities I highly encourage you to install all the python packages in a new environment. Think of an environment as an isolated area to install the software packages you need for a specific project, i.e. in this case the course activities. Packages in an environment are isolated from other software packages on your computer. An environment
   - **Best practice:** create a new environment for each of your projects.
   - **Isolation:** is typically defined in a specific folder on your computer.
   - **Experimentation:** allows experimenting with installation of new packages without disrupting packages in other environments 
   - **Multiple projects:** allows you to manage conflicting packages in separate environments

### VSCode (Windows, Mac, Linux)

Download and install [Visual Studio Code](https://code.visualstudio.com/docs/setup/setup-overview) from the official website. Follow the platform-specific installation instructions for your operating system (Windows, macOS, or Linux).

### Windows (Tools & Python)

Since we're using the Linux command line, you will need to install a Linux-like terminal program. I recommend installing Git-Bash which provides the Linux-style terminal and also Git.

1. Install Git-Bash: Download and install Git-Bash from the [official Git website](https://git-scm.com/downloads).
2. Download the Miniforge Installer: Go to the [conda-forge Miniforge GitHub repository](https://github.com/conda-forge/miniforge) and download the Windows executable file (Miniforge3-Windows-x86_64.exe).
3. Run the Executable Installer: Double-click the downloaded .exe file to run the installer.
   - Follow the prompts, accepting the license agreement.
   - It is highly recommended to install for "Just Me" (per user) to avoid potential permission issues later.
   - Note the installation path: The default installation path is usually within your AppData\Local folder (e.g., C:\Users\YOUR_USERNAME\AppData\Local\miniforge3). Remember this location.
   - Check the "Create start menu shortcuts" option. The most convenient and tested way to use the installed software (such as commands conda and mamba) is via the "Miniforge Prompt" installed to the start menu.
   - Check the "Add Miniforge3 to my PATH environment variable" option. 
4. Create a conda (mamba) environment. In your terminal execute the following command
   ```bash
   mamba env create -n ds2002 -c conda-forge python=3.11 htop jq awscli curl wget git zip unzip tar redis-server redis-py mongodb
   ```
5. Configure Git Bash: After the installation is complete, you need to configure Git Bash to recognize the conda commands.
   - Open a Git Bash terminal.
   - Run the following command to update your ~/.bashrc file. Adjust the path if you installed Miniforge in a non-default location (see step 3):
      ```bash
      echo "source ~/AppData/Local/miniforge3/etc/profile.d/conda.sh" >> ~/.bashrc
      ```
6. Restart Git Bash and Verify:
   - Close and re-open your Git Bash terminal for the changes to take effect.
   - Run `conda activate ds2002`. The prompt should change from `base` to `ds2002` indicating the switch to your new environment.
   - Run the command `conda list`. You should see a list of installed packages, and your prompt should show (ds2002) at the beginning, confirming that the ds2002 environment is active.

**Note: The first step when opening a new terminal is to run `conda activate ds2002`.** You can add that command to the ~/.bashrc file if you wish.


### MacOS, Linux (Tools & Python)

MacOS and Linux have terminal applications pre-installed. So you won't need Git-Bash. Follow these steps to install miniforge for Python.

1. Open a terminal window.
2. Download the installer script: The command below automatically detects your system's architecture and downloads the correct Miniforge3 installer from the official conda-forge GitHub repository.
   ```bash
   curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh
   ```
   **Note:** For some specific macOS architectures (like Apple Silicon/arm64), the command might be slightly different; you can check the [Miniforge GitHub page](https://github.com/conda-forge/miniforge) for direct links if the automatic detection fails.
3. Run the installation script: Execute the downloaded script using bash.
   ```bash
   bash Miniforge3-$(uname)-$(uname -m).sh
   ```
   Alternatively, if the automatic detection in the filename does not work, you can use a fixed filename after downloading it, for example:
   ```bash
   bash Miniforge3.sh
   ```
   Follow the prompts: The installer will guide you through the process.
   - Press ENTER or return to view the license agreement.
   - Scroll through the license and type `yes` to accept the terms.
   - Confirm the default installation location (typically ~/miniforge3). Press ENTER to accept it.
   - When asked if you want to initialize Conda for your shell (e.g., bash or zsh), type `yes`.
4. Restart your terminal: For the changes to take effect, close your current terminal window and open a new one.
5. Verify the installation:
   - Once the terminal is restarted, you should see `(base)` in your terminal prompt, indicating the Miniforge base environment is active.
   - Run the following command to verify:
     ```bash
     conda list
     ```
   - If a list of installed packages appears without errors, the installation was successful. 
6. Create a conda (mamba) environment and install the other software packages. In your terminal execute the following command:
   ```bash
   mamba env create -n ds2002 -c conda-forge python=3.11 htop jq awscli curl wget git zip unzip tar redis-server redis-py mongodb
   ```
   
   Run the command `conda activate ds2002` to activate the environment, then run `conda list`. You should see a list of installed packages, and your prompt should show (ds2002) at the beginning, confirming that the ds2002 environment is active.

**Note: The first step when opening a new terminal is to run `conda activate ds2002`.** If your Mac is using zsh and throws an error, you can use `source activate ds2002` instead. You can add that command to the ~/.bashrc (or .zshrc) file if you wish.

**Please be aware that we have limited bandwidth to guide you through fixing broken installations on your computer. If installations fail, you can always go back to using GitHub Codespaces.**

