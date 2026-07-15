provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "kcn" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.large"

  tags = {
    Name = "KCN-Intelligence-OS"
  }
}
