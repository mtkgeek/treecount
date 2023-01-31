## Geoscripting project repository.

- Title: Tree species recognition from drone imagery 
- Team name and members: Agile Dodo of Weather Magic
- Challenge number (or "own"): 2
- Description, how to run/reproduce:





## SET UP
1. Update R to at least version 4.2.2
    Run the following  commands on your terminal
    - `wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc`
    - `sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"`
    - `sudo apt update`
    - `sudo apt install --no-install-recommends r-base`

2. Download X11 development libraries in case you don't have them. Run the following in your terminal
    - `sudo apt install libx11-dev`