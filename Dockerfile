FROM ohshin/ubot:dev

WORKDIR /bottol
RUN chmod 777 /bottol

# Installing Requirements
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# If u want to use /update feature, uncomment the following and edit
#RUN git config --global user.email "your_email"
#RUN git config --global user.name "git_username"

# Copying All Source
COPY . .

CMD ["bash","start"]
####CMD ["python3", "-m", "ubot"]
