# Required due to VirtualBox Guest Addition probles caused by
# different Versions of VirtualBox
unless Vagrant.has_plugin?("vagrant-vbguest")
    raise Vagrant::Errors::VagrantError.new, "Plugin missing: vagrant-vbguest - please install via vagrant plugin install"
end

Vagrant.configure("2") do |config|
  
  # Configures how much memory goes to the machine
  # This can be adjusted by editing the 2024 to a different value (more than 512)
  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "2024"]
  end

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network :forwarded_port, guest: 80, host: 8080

  # Makes the entire CSV-Tools directory available as is
  config.vm.synced_folder "~/Work/School/SEW", "/home/vagrant/CSV-Tools"

  # Install project dependicies
  config.vm.provision :shell, :path => "./install.sh"
end
