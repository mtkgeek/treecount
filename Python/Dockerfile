# Source: https://blog.somideolaoye.com/fastapi-deploy-containerized-apps-on-google-cloud-run


FROM python:3.8.10
# 


WORKDIR /code

# Source: https://www.r-bloggers.com/2022/08/installation-of-r-4-2-on-ubuntu-22-04-1-lts-and-tips-for-spatial-packages/
# install R on the server

# RUN apt-get update
RUN apt-get -y dist-upgrade
# install R on the server
RUN apt install -y --no-install-recommends software-properties-common dirmngr
# Add the keys
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
# add the R 4.0 repo from CRAN -- adjust 'focal' to 'groovy' or 'bionic' as needed
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/"
RUN apt install -y --no-install-recommends r-base
RUN apt install libx11-dev


# RUN apt-get install r-base-dev=4.2.2

# RUN apt-get update
# RUN apt-get install -y gdebi-core
# RUN curl -O https://cdn.rstudio.com/r/ubuntu-2004/pkgs/r-4.2.2_1_amd64.deb
# RUN gdebi -n r-4.2.2_1_amd64.deb

# Enable the Extra Packages for Enterprise Linux (EPEL) repository
RUN apt-get install -y yum

# RUN \
#     yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
#     yum install yum-utils && \
#     yum-config-manager --enable "rhel-*-optional-rpms" && \
#     curl -O https://cdn.rstudio.com/r/centos-7/pkgs/R-4.1.3-1-1.x86_64.rpm && \
#     yum install R-4.1.3-1-1.x86_64.rpm


# RUN apt install -y libgdal-dev libproj-dev libgeos-dev libudunits2-dev libv8-dev libnode-dev libcairo2-dev libnetcdf-dev


RUN R -e "install.packages('ForestTools', repos='http://cran.us.r-project.org')"
RUN R -e "install.packages('rgdal', repos='http://cran.us.r-project.org')"


# ENV R_HOME /usr/lib/R


COPY ./requirements.txt /code/requirements.txt

# 
RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 


COPY ./app /code/app

# 

ENTRYPOINT ["python3", "app/main.py"]
