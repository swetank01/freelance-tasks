data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name = "name"
    values = [
      "ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*",
    ]
  }
  owners = ["099720109477"] 
}

resource "aws_instance" "python-server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
  key_name      = "swetank-mac-aws"
  user_data = "${file("install_python_server.sh")}"
  vpc_security_group_ids = ["${aws_security_group.sg_allow_ssh_nginx.id}"]

  tags = {
    Name = "python-server"
  }
}