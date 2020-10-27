Name: firmware-imx
Version: 8.9
Release: alt1

Summary: NXP iMX BSP firmware
License: GPL
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

%description
NXP iMX BSP firmware

%prep
%setup

%build

%install
mkdir -p %{buildroot}/lib/firmware/imx
for i in ddr epdc hdmi sdma vpu; do
    cp -a firmware-imx/firmware/$i %{buildroot}/lib/firmware/imx/
done

%files
/lib/firmware/imx

%changelog
* Tue Oct 27 2020 Pavel Nakonechnyi <zorg@altlinux.org> 8.9-alt1
- updated to version 8.9

* Wed Dec 25 2019 Pavel Nakonechnyi <zorg@altlinux.org> 8.5-alt1
- updated to version 8.5

* Sun Jul 07 2019 Pavel Nakonechnyi <zorg@altlinux.org> 8.1-alt1
- initial build of iMX BSP firmware
