Summary:	A command line CD/DVD-Recorder
Summary(pt_BR):	Um programa de gravaГЦo de CD/DVD.
Summary(es):	Un programa de grabaciСn de CD/DVD.
Summary(pl):	Program do nagrywania pЁyt CD/DVD
Summary(pt_BR):	Um programa de gravaГЦo de CD/DVD.
Summary(ru):	Программа для записи CD/DVD, запускаемая из командной строки
Summary(uk):	Програма для запису CD/DVD, яка запуска╓ться з командно╖ стр╕чки
Name:		cdrtools
Version:	2.01a14
Release:	1
Epoch:		2
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.berlios.de/pub/cdrecord/alpha/%{name}-%{version}.tar.bz2
Patch0:		%{name}-config.patch
Patch1:		%{name}-smmap.patch
Patch2:		%{name}-silo.patch
Patch3:		%{name}-man.patch
Patch4:		%{name}-u8-type.aptch
URL:		http://www.fokus.gmd.de/research/cc/glone/employees/joerg.schilling/private/cdrecord.html
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	cdrecord
Provides:	cdrecord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdrecord allows you to create CD's on a CD-Recorder (SCSI/ATAPI).
Supports data, audio, mixed, multi-session and CD+ discs etc.

%description -l pl
Cdrecord pozwala tworzyФ CD na nagrywarce CD (SCSI/ATAPI). ObsЁuguje
dyski z danymi, d╪wiЙkiem, mieszane, wielosesyjne, CD+ i inne.

%description -l pt_BR
Cdrecord permite que vocЙ crie CDs em seu gravador de CDs SCSI/ATAPI.
и possМvel gravar dados, Аudio, misturados, multi-seГЦo e CD+.

%description -l ru
Cdrecord - это программа для создания аудио и цифровых CD. Cdrecord
работает со многими типами CD-рекордеров разных производителей,
полностью поддерживает multi-session и сообщает об ошибках в формате,
пригодном для чтения человеком.

%description -l uk
Cdrecord - це програма для створення ауд╕о та програмних CD. Cdrecord
працю╓ з багатьма типами CD-рекордер╕в р╕зних виробник╕в, повн╕стю
п╕дтриму╓ multi-session ╕ пов╕домля╓ про помилки у формат╕, придатному
для читання людиною.

%package devel
Summary:	The libschily SCSI user level transport library
Summary(es):	La biblioteca SCSI libschily
Summary(pl):	Biblioteka dostЙpu do poziomu SCSI przez u©ytkownika
Summary(pt_BR):	A biblioteca SCSI libschily
Summary(ru):	SCSI-библиотека libschily
Summary(uk):	SCSI-б╕бл╕отека libschily
Group:		Development/Libraries
Obsoletes:	cdrecord-devel

%description devel
The %{name} distribution contains a SCSI user level transport library.
The SCSI library is suitable to talk to any SCSI device without having
a special driver for it. Cdrecord may be easily ported to any system
that has a SCSI device driver similar to the scg driver.

%description devel -l pl
Dystrybucja %{name} zawiera bibliotekЙ dostЙpu do warstwy transportu w
SCSI. Poprzez bibliotekЙ mo©na komunikowaФ siЙ z dowolnym urz╠dzeniem
SCSI bez potrzeby posiadania specjalnego sterownika do tego
urz╠dzenia.

%description devel -l pt_BR
O cdrtools contИm uma biblioteca de transporte de dados por SCSI "user
level". A biblioteca SCSI pode ser usada para conversar com qualquer
dispositivo SCSI sem a necessidade de um driver especial.

%description devel -l ru
Пакет cdrecord-devel содержит транспортные библиотеки
пользовательского уровня для SCSI, которые могут работать с любым
SCSI-устройством без специального драйвера для этого устройства.
Cdrecord может быть легко портирован на любую систему с драйвером
SCSI-устройства, похожим на драйвер scg.

%description devel -l uk
Пакет cdrecord-devel м╕стить транспортн╕ б╕бл╕отеки користувацького
р╕вня для SCSI, як╕ можуть працювати з будь-яким SCSI-пристро╓м без
спец╕ального драйвера для цього пристрою. Cdrecord може бути легко
портований на будь-яку систему з драйвером SCSI-пристроя, схожим на
драйвер scg.

%package cdda2wav
Summary:	Get WAV files from digital audio cd's
Summary(es):	Crea archivos tipo WAV a partir de CDs de audio.
Summary(fr):	convertisseur CD-Audio->.wav
Summary(pl):	Uzyskaj pliki WAV z cyfrowego kompaktu audio
Summary(pt_BR):	Cria arquivos tipo WAV a partir de CDs de Аudio.
Summary(ru):	Утилита для получения файлов .wav с digital audio CD
Summary(uk):	Утил╕та для генерац╕╖ файл╕в .wav з digital audio CD
Group:		Applications/Sound
Provides:	cdda2wav
Obsoletes:	cdda2wav
Obsoletes:	cdrecord-cdda2wav

%description cdda2wav
A sampling utility for cdrom drives that are capable of sending audio
cd data in digital form to your host. Data can be dumped into wav or
sun format sound files. Options control the recording format
(stereo/mono; 8,12,16 bits; different rates).

%description cdda2wav -l es
Un utilitario para leer mЗsicas en accionadores de cdrom capaces de
transmitir datos de CDs de audio en forma digital para tu mАquina. Los
datos pueden ser grabados en formato wav o sun. Existen opciones para
controlar el formato de la grabaciСn (stereo/mono, 8, 12, 16 bits,
tasas diferentes).

%description cdda2wav -l pl
NarzЙdzie do zczytywania danych z napЙdСw cdrom, ktСre s╠ w stanie
wysyЁaФ strumieЯ audio. Dane mog╠ zostaФ zapisane w formacie plikСw
wav lub suna.

%description cdda2wav -l pt_BR
Um utilitАrio para ler mЗsicas em acionadores de cdrom capazes de
transmitir dados de CDs de Аudio em forma digital para sua mАquina. Os
dados podem ser gravados em formato wav ou sun. Existem opГУes para
controlar o formato da gravaГЦo (estИreo/mono, 8, 12, 16 bits, taxas
diferentes).

%description cdda2wav -l ru
Cdda2wav - это сэмплер, способный считывать аудиоданные с CD в
цифровой форме и сохранять их на диск в виде звуковых файлов формата
.wav или .sun. Форматы записи включают стерео/моно, 8/12/16 бит и
различные частоты дискретизации. Cdda2wav также может быть использован
как CD-плейер.

%description cdda2wav -l uk
Cdda2wav - це семплер, здатний зчитувати ауд╕одан╕ ╕ CD у цифров╕й
форм╕ та збер╕гати ╖х на диск у вигляд╕ звукових файл╕в формату .wav
або .sun. Формати запису включають стерео/моно, 8/12/16 б╕т та р╕зн╕
частоты дискретизац╕╖. Cdda2wav також може бути використаний як
CD-плей╓р.

%package readcd
Summary:	Read/Write data Compact Discs
Summary(pl):	Odczytuje/Zapisuje dane z PЁyt Kompaktowych
Group:		Applications/System
Obsoletes:	cdrecord-readcd

%description readcd
Read/Write data Compact Discs

%description readcd -l pl
Odczytuje/Zapisuje dane z PЁyt Kompaktowych

%package utils
Summary:	Dumping and verifying iso9660 images
Summary(pl):	Zrzucanie i weryfikacja obrazСw iso9660
Group:		Applications/System

%description utils
Utility programs for dumping and verifying iso9660 images.

%description utils -l pl
NarzЙdzia do zrzucania i weryfikacji obrazСw iso9660.

%package mkisofs
Summary:	Creates an ISO9660 filesystem image
Summary(de):	Erstellt ein Dateisystem-Abbild nach ISO9660
Summary(es):	Crea una imagen de un sistema de archivos ISO9660
Summary(fr):	CrИe un image systХme de fichiers ISO9660
Summary(pl):	Tworzy obraz systemu plikСw ISO9660
Summary(pt_BR):	Cria uma imagem de um sistema de arquivos ISO9660
Summary(ru):	Создает образ файловой системы ISO9660
Summary(tr):	ISO9660 dosya sistemi kopyasЩ oluЧturur
Summary(uk):	Створю╓ образ файлово╖ системи ISO9660
Group:		Applications/System
Provides:	mkisofs
Obsoletes:	mkisofs

%description mkisofs
This is the mkisofs package. It is used to create ISO 9660 file system
images for creating CD-ROMs.

%description mkisofs -l es
Este es el paquete mkisofs. Se le usa para crear imАgenes de sistema
de archivos ISO 9660 en la creaciСn de CD-ROMs. Ahora incluye soporte
para hacer CD-ROMs de boot "El Torito".

%description mkisofs -l pl
To jest pakiet mkisofs. Jest on u©ywany do tworzenia obrazСw systemСw
plikСw ISO9660 potrzebnych do tworzenia pЁyt CD-ROM.

%description mkisofs -l pt_BR
Este И o pacote mkisofs. Ele И usado para criar imagens de sistema de
arquivos ISO 9660 para criaГЦo de CD-ROMs. Agora inclui suporte para
fazer CD-ROMs de boot "El Torito".

%description mkisofs -l ru
Программа mkisofs используется для подготовки мастер-диска, т.е. она
генерирует файловую систему ISO9660. Mkisofs делает снимок заданного
дерева каталогов и генерирует бинарный образ этого дерева, который
соответствует файловой системе ISO9660, записываемой на блочное
устройство. Mkisofs используется для записи CD-ROM'ов и включает
поддержку создания загружаемых El Torito CD-ROM'ов.

%description mkisofs -l uk
Програма mkisofs використову╓ться для п╕дготовки мастер-диску, вона
генеру╓ файлову систему ISO9660. Mkisofs робить зн╕мок заданого дерева
каталог╕в та генеру╓ б╕нарный образ цього дерева, який в╕дпов╕да╓
файлов╕й систем╕ ISO9660, записуван╕й на блочний пристр╕й. Mkisofs
використову╓ться для запису CD-ROM'╕в ╕ ма╓ п╕дтримку створення
завантажуваних El Torito CD-ROM'╕в.

%prep
%setup -q -n cdrtools-2.01
chmod +w -R *
%patch0 -p1
%patch1 -p1
%ifarch sparc sparcv9 sparc64
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1

%build
cd conf
cp xconfig.h.in xconfig.h.in.org
sed -e 's#/\*.*\*/##g' xconfig.h.in.org > xconfig.h.in
rm -f acgeneral.m4 acspecific.m4 autoheader.m4 acoldnames.m4 autoconf.m4
%{__aclocal}
%{__autoconf}
cd ..
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" ./Gmake.linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_includedir}/schily/scg}

./Gmake.linux install \
	MANDIR=share/man \
	INS_BASE=$RPM_BUILD_ROOT%{_prefix}

install cdda2wav/cdda2mp3	$RPM_BUILD_ROOT%{_bindir}/
install cdda2wav/cdda2ogg	$RPM_BUILD_ROOT%{_bindir}/

# Installing Header files for use with devel package
rm -f include/scg

install include/*		$RPM_BUILD_ROOT%{_includedir}/schily
install incs/*/xconfig.h	$RPM_BUILD_ROOT%{_includedir}/schily
install libscg/scg/*		$RPM_BUILD_ROOT%{_includedir}/schily/scg

install cdrecord/cdrecord.dfl	$RPM_BUILD_ROOT%{_sysconfdir}/cdrecord.conf

# fix manual pages
echo ".so man8/isoinfo.8" >	$RPM_BUILD_ROOT%{_mandir}/man8/devdump.8
echo ".so man8/isoinfo.8" >     $RPM_BUILD_ROOT%{_mandir}/man8/isovfy.8
echo ".so man8/isoinfo.8" >     $RPM_BUILD_ROOT%{_mandir}/man8/isodump.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AN-* doc/cdrecord.ps Changelog README README.ATAPI README.DiskT@2
%doc README.WORM README.audio README.cdplus README.cdtext README.cdrw
%doc README.copy README.linux README.mkisofs README.multi README.parallel
%doc README.raw README.rscsi README.sony README.verify make_diskt@2.sh
%doc cdrecord/cdrecord.dfl cdrecord/LICENSE
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cdrecord.conf
%attr(755,root,root) %{_bindir}/cdrecord
%attr(755,root,root) %{_bindir}/scgcheck
%attr(755,root,root) %{_sbindir}/rscsi
%{_mandir}/man1/cdrecord.1*
%{_mandir}/man1/scgcheck.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/schily
%{_includedir}/*.h
#%attr(755,root,root) %{_bindir}/scgcheck
#%%{_mandir}/man1/scgcheck.1*

%files cdda2wav
%defattr(644,root,root,755)
%doc cdda2wav/Frontends cdda2wav/HOWTOUSE cdda2wav/OtherProgs
%doc cdda2wav/README cdda2wav/THANKS cdda2wav/TODO
%doc cdda2wav/cdda2mp3.new cdda2wav/cdda_links cdda2wav/pitchplay
%doc cdda2wav/readmult cdda2wav/tracknames.pl cdda2wav/tracknames.txt
%doc cdda2wav/FAQ
%attr(755,root,root) %{_bindir}/cdda2wav
%attr(755,root,root) %{_bindir}/cdda2mp3
%attr(755,root,root) %{_bindir}/cdda2ogg
%{_mandir}/man1/cdda2wav.1*
%{_mandir}/man1/cdda2ogg.1*

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
%attr(755,root,root) %{_bindir}/isodebug
%attr(755,root,root) %{_bindir}/isoinfo
%attr(755,root,root) %{_bindir}/isovfy
%attr(755,root,root) %{_bindir}/isodump

%files mkisofs
%defattr(644,root,root,755)
%{_mandir}/man8/mkisofs.8*
%{_mandir}/man8/mkhybrid.8*
%attr(755,root,root) %{_bindir}/mkisofs
%attr(755,root,root) %{_bindir}/mkhybrid
%doc mkisofs/README.compression mkisofs/README.eltorito mkisofs/README
%doc mkisofs/README.graft_dirs mkisofs/README.hfs_boot mkisofs/README.hfs_magic
%doc mkisofs/README.hide mkisofs/README.joliet mkisofs/README.mkhybrid
%doc mkisofs/README.prep_boot mkisofs/README.rootinfo mkisofs/README.session
%doc mkisofs/README.sort mkisofs/README.sparcboot
