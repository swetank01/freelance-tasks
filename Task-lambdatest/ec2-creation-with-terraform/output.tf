output "server_ip_address" {
  value = "${aws_instance.python-server.public_dns}"
}