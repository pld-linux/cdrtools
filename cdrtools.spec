%define	ver	1.10
Summary:	A command line CD/DVD-Recorder
Summary(pl):	Program do nagrywania p³yt CD/DVD
Name:		cdrtools
Version:	%{ver}a10
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.fokus.gmd.de/pub/unix/cdrecord/alpha/%{name}-%{version}.tar.gz
Patch0:		cdrecord-config.patch
URL:		http://www.fokus.gmd.de/research/cc/glone/employees/joerg.schilling/private/cdrecord.html
Obsoletes:	cdrecord
Provides:	cdrecord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdrecord allows you to create CD's on a CD-Recorder (SCSI/ATAPI).
Supports data, audio, mixed, multi-session and CD+ discs etc.

%description -l pl
Cdrecord pozwala tworzyæ CD na nagrywarce CD (SCSI/ATAPI). Obs³uguje
dyski z danymi, d¼wiêkiem, mieszane, wielosesyjne, CD+ i inne.

%package devel
Summary:	The libschily SCSI user level transport library
Summary(pl):	Biblioteka dostêpu do poziomu SCSI przez u¿ytkownika
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Obsoletes:	cdrecord-devel

%description devel
The %{name} distribution contains a SCSI user level transport library.
The SCSI library is suitable to talk to any SCSI device without having
a special driver for it. Cdrecord may be easily ported to any system
that has a SCSI device driver similar to the scg driver.

%description devel -l pl
Dystrybucja %{name} zawiera bibliotekê dostêpu do warstwy transportu w
SCSI. Poprzez bibliotekê mo¿na komunikowaæ siê z dowolnym urz±dzeniem
SCSI bez potrzeby posiadania specjalnego sterownika do tego
urz±dzenia.

%package cdda2wav
Summary:	Get WAV files from digital audio cd's
Summary(pl):	Uzyskaj pliki WAV z cyfrowego kompaktu audio
Summary(fr):	convertisseur CD-Audio->.wav
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Provides:	cdda2wav
Obsoletes:	cdda2wav

%description cdda2wav
A sampling utility for cdrom drives that are capable of sending audio
cd data in digital form to your host. Data can be dumped into wav or
sun format sound files. Options control the recording format
(stereo/mono; 8,12,16 bits; different rates).

%description -l pl cdda2wav
Narzêdzie do zczytywania danych z napêdów cdrom, które s± w stanie
wysy³aæ strumieñ audio. Dane mog± zostaæ zapisane w formacie plików
wav lub suna.

%package readcd
Summary:	Read/Write data Compact Discs
Summary(pl):	Odczytuje/Zapisuje dane z P³yt Kompaktowych
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description readcd
Read/Write data Compact Discs

%description -l pl readcd
Odczytuje/Zapisuje dane z P³yt Kompaktowych

%package utils
Summary:	Dumping and verifying iso9660 images.
Summary(pl):	Zrzucanie i weryfikacja obrazów iso9660.
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description utils
Utility programs for dumping and verifying iso9660 images.

%description -l pl utils
Narzêdzia do zrzucania i weryfikacji obrazów iso9660.

%package mkisofs
Summary:	Creates an ISO9660 filesystem image
Summary(de):	Erstellt ein Dateisystem-Abbild nach ISO9660
Summary(fr):	Crée un image système de fichiers ISO9660
Summary(pl):	Tworzy obraz systemu plikow ISO9660
Summary(tr):	ISO9660 dosya sistemi kopyasý oluþturur
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Provides:	mkisofs
Obsoletes:	mkisofs

%description mkisofs
This is the mkisofs package. It is used to create ISO 9660 file system
images for creating CD-ROMs.

%description -l pl mkisofs
To jest pakiet mkisofs. Jest on u¿ywany do tworzenia obrazów systemów
plików ISO9660 potrzebnych do tworzenia p³yt CD-ROM.

%prep
%setup -q -n %{name}-%{ver}
%patch0 -p1

%build
CFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}" LDFLAGS="%{!?debug:-s}" ./Gmake.linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_includedir}/schily/scg}
./Gmake.linux install \
	MANDIR=share/man \
	INS_BASE=$RPM_BUILD_ROOT%{_prefix}

# Installing Header files for use with devel package
rm -f include/scg

install include/*		$RPM_BUILD_ROOT%{_includedir}/schily
install libscg/scg/*		$RPM_BUILD_ROOT%{_includedir}/schily/scg

install cdrecord/cdrecord.dfl	$RPM_BUILD_ROOT%{_sysconfdir}/cdrecord.conf

# fix manual pages
echo "man8/isoinfo.so" >	$RPM_BUILD_ROOT%{_mandir}/man8/devdump.8
echo "man8/isoinfo.so" >        $RPM_BUILD_ROOT%{_mandir}/man8/isovfy.8
echo "man8/isoinfo.so" >        $RPM_BUILD_ROOT%{_mandir}/man8/isodump.8

gzip -9nf AN-%{version} doc/cdrecord.ps Changelog README \
	README.ATAPI README.WORM README.audio README.cdplus \
	README.cdrw README.linux README.mkisofs README.multi \
	README.sony README.verify README.copy Linux.scsi-patch \
	cdda2wav/Frontends cdda2wav/HOWTOUSE cdda2wav/OtherProgs \
	cdda2wav/README cdda2wav/THANKS cdda2wav/TODO cdda2wav/cdda2mp3 \
	cdda2wav/cdda2mp3.new cdda2wav/cdda_links cdda2wav/pitchplay \
	cdda2wav/readmult cdda2wav/tracknames.pl cdda2wav/tracknames.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AN-%{version},doc/cdrecord.ps,Changelog,README}.gz
%doc {README.ATAPI,README.WORM,README.audio,README.cdplus}.gz
%doc {README.cdrw,README.linux,README.mkisofs,README.multi}.gz
%doc {README.sony,README.verify,README.copy,Linux.scsi-patch}.gz
%doc cdrecord/cdrecord.dfl
%config(noreplace) %{_sysconfdir}/cdrecord.conf
%attr(755,root,root) %{_bindir}/cdrecord
%{_mandir}/man1/cdrecord.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdeflt.a
%{_libdir}/libscg.a
%{_libdir}/libschily.a
%{_includedir}/schily
%{_includedir}/*.h

%files cdda2wav
%defattr(644,root,root,755)
%doc {cdda2wav/Frontends,cdda2wav/HOWTOUSE,cdda2wav/OtherProgs}.gz
%doc {cdda2wav/README,cdda2wav/THANKS,cdda2wav/TODO,cdda2wav/cdda2mp3}.gz
%doc {cdda2wav/cdda2mp3.new,cdda2wav/cdda_links,cdda2wav/pitchplay}.gz
%doc {cdda2wav/readmult,cdda2wav/tracknames.pl,cdda2wav/tracknames.txt}.gz
%doc AN-%{version}.gz
%attr(755,root,root) %{_bindir}/cdda2wav
%{_mandir}/man1/cdda2wav.1*

%files readcd
%defattr(644,root,root,755)
%{_mandir}/man1/readcd.1*
%attr(755,root,root) %{_bindir}/readcd

%files utils
%defattr(644,root,root,755)
%{_mandir}/man8/isoinfo.8*
%{_mandir}/man8/devdump.8*
%{_mandir}/man8/isovfy.8*
%{_mandir}/man8/isodump.8*
%attr(755,root,root) %{_bindir}/devdump
%attr(755,root,root) %{_bindir}/isoinfo
%attr(755,root,root) %{_bindir}/isovfy
%attr(755,root,root) %{_bindir}/isodump

%files mkisofs
%defattr(644,root,root,755)
%{_mandir}/man8/mkisofs.8*
%{_mandir}/man8/mkhybrid.8*
%attr(755,root,root) %{_bindir}/mkisofs
%attr(755,root,root) %{_bindir}/mkhybrid
