Summary:	Highly portable CD/DVD/BluRay command line recording software
Summary(es.UTF-8):	Un programa de grabación de CD/DVD/BluRay
Summary(pl.UTF-8):	Oprogramowanie do nagrywania płyt CD/DVD/BluRay
Summary(pt_BR.UTF-8):	Um programa de gravação de CD/DVD/BluRay
Summary(ru.UTF-8):	Программа для записи CD/DVD/BluRay, запускаемая из командной строки
Summary(uk.UTF-8):	Програма для запису CD/DVD/BluRay, яка запускається з командної стрічки
Name:		cdrtools
Version:	3.01
Release:	1
Epoch:		5
License:	GPL v2 (mkisofs), CDDL v1.0 (the rest)
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/cdrtools/%{name}-%{version}.tar.bz2
# Source0-md5:	7d45c5b7e1f78d85d1583b361aee6e8b
Patch0:		%{name}-config.patch
Patch2:		%{name}-man.patch
Patch3:		%{name}-make.patch
Patch4:		%{name}-linking.patch
Patch5:		%{name}-revert_sg_io_eperm_failure.patch
URL:		http://cdrtools.sourceforge.net/
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	iconv
BuildRequires:	libcap-devel
Provides:	cdrecord
Obsoletes:	cdrecord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-finput-charset=ISO-8859-1 -fexec-charset=UTF-8 -D__attribute_const__=const

%ifarch %{ix86}
%define		parch		i686
%endif
%ifarch %{x8664}
%define		parch		amd64
%endif
%ifnarch %{ix86} %{x8664}
%define		parch		%{_arch}
%endif

%description
Cdrtools is a set of command line programs that allows to record
CD/DVD/BluRay media.

%description -l pl.UTF-8
Cdrtools jest zestawemn narzędzi pozwalającym na nagrywanie płyt
CD/DVD/BluRay z linii poleceń.

%description -l pt_BR.UTF-8
Cdrecord permite que você crie CDs em seu gravador de CDs SCSI/ATAPI.
É possível gravar dados, áudio, misturados, multi-seção e CD+.

%description -l ru.UTF-8
Cdrecord - это программа для создания аудио и цифровых CD. Cdrecord
работает со многими типами CD-рекордеров разных производителей,
полностью поддерживает multi-session и сообщает об ошибках в формате,
пригодном для чтения человеком.

%description -l uk.UTF-8
Cdrecord - це програма для створення аудіо та програмних CD. Cdrecord
працює з багатьма типами CD-рекордерів різних виробників, повністю
підтримує multi-session і повідомляє про помилки у форматі, придатному
для читання людиною.

%package devel
Summary:	The libschily SCSI user level transport library
Summary(es.UTF-8):	La biblioteca SCSI libschily
Summary(pl.UTF-8):	Biblioteka dostępu do poziomu SCSI przez użytkownika
Summary(pt_BR.UTF-8):	A biblioteca SCSI libschily
Summary(ru.UTF-8):	SCSI-библиотека libschily
Summary(uk.UTF-8):	SCSI-бібліотека libschily
Group:		Development/Libraries
Obsoletes:	cdrecord-devel

%description devel
The %{name} distribution contains a SCSI user level transport library.
The SCSI library is suitable to talk to any SCSI device without having
a special driver for it. Cdrecord may be easily ported to any system
that has a SCSI device driver similar to the scg driver.

%description devel -l pl.UTF-8
Dystrybucja %{name} zawiera bibliotekę dostępu do warstwy transportu w
SCSI. Poprzez bibliotekę można komunikować się z dowolnym urządzeniem
SCSI bez potrzeby posiadania specjalnego sterownika do tego
urządzenia.

%description devel -l pt_BR.UTF-8
O cdrtools contém uma biblioteca de transporte de dados por SCSI "user
level". A biblioteca SCSI pode ser usada para conversar com qualquer
dispositivo SCSI sem a necessidade de um driver especial.

%description devel -l ru.UTF-8
Пакет cdrecord-devel содержит транспортные библиотеки
пользовательского уровня для SCSI, которые могут работать с любым
SCSI-устройством без специального драйвера для этого устройства.
Cdrecord может быть легко портирован на любую систему с драйвером
SCSI-устройства, похожим на драйвер scg.

%description devel -l uk.UTF-8
Пакет cdrecord-devel містить транспортні бібліотеки користувацького
рівня для SCSI, які можуть працювати з будь-яким SCSI-пристроєм без
спеціального драйвера для цього пристрою. Cdrecord може бути легко
портований на будь-яку систему з драйвером SCSI-пристроя, схожим на
драйвер scg.

%package cdda2wav
Summary:	Get WAV files from digital audio cd's
Summary(es.UTF-8):	Crea archivos tipo WAV a partir de CDs de audio
Summary(fr.UTF-8):	convertisseur CD-Audio->.WAV
Summary(pl.UTF-8):	Uzyskaj pliki WAV z cyfrowego kompaktu audio
Summary(pt_BR.UTF-8):	Cria arquivos tipo WAV a partir de CDs de áudio
Summary(ru.UTF-8):	Утилита для получения файлов .WAV с digital audio CD
Summary(uk.UTF-8):	Утиліта для генерації файлів .WAV з digital audio CD
Group:		Applications/Sound
Provides:	cdda2wav
Obsoletes:	cdda2wav
Obsoletes:	cdrecord-cdda2wav

%description cdda2wav
A sampling utility for cdrom drives that are capable of sending audio
cd data in digital form to your host. Data can be dumped into WAV or
sun format sound files. Options control the recording format
(stereo/mono; 8,12,16 bits; different rates).

%description cdda2wav -l es.UTF-8
Un utilitario para leer músicas en accionadores de cdrom capaces de
transmitir datos de CDs de audio en forma digital para tu máquina. Los
datos pueden ser grabados en formato WAV o sun. Existen opciones para
controlar el formato de la grabación (stereo/mono, 8, 12, 16 bits,
tasas diferentes).

%description cdda2wav -l pl.UTF-8
Narzędzie do zczytywania danych z napędów cdrom, które są w stanie
wysyłać strumień audio. Dane mogą zostać zapisane w formacie plików
WAV lub suna.

%description cdda2wav -l pt_BR.UTF-8
Um utilitário para ler músicas em acionadores de cdrom capazes de
transmitir dados de CDs de áudio em forma digital para sua máquina. Os
dados podem ser gravados em formato WAV ou sun. Existem opções para
controlar o formato da gravação (estéreo/mono, 8, 12, 16 bits, taxas
diferentes).

%description cdda2wav -l ru.UTF-8
Cdda2wav - это сэмплер, способный считывать аудиоданные с CD в
цифровой форме и сохранять их на диск в виде звуковых файлов формата
.WAV или .sun. Форматы записи включают стерео/моно, 8/12/16 бит и
различные частоты дискретизации. Cdda2wav также может быть использован
как CD-плейер.

%description cdda2wav -l uk.UTF-8
Cdda2wav - це семплер, здатний зчитувати аудіодані і CD у цифровій
формі та зберігати їх на диск у вигляді звукових файлів формату .WAV
або .sun. Формати запису включають стерео/моно, 8/12/16 біт та різні
частоты дискретизації. Cdda2wav також може бути використаний як
CD-плейєр.

%package readcd
Summary:	Read/Write data Compact Discs
Summary(pl.UTF-8):	Odczytuje/Zapisuje dane z Płyt Kompaktowych
Group:		Applications/System
Obsoletes:	cdrecord-readcd

%description readcd
Read/Write data Compact Discs.

%description readcd -l pl.UTF-8
Odczytuje/Zapisuje dane z Płyt Kompaktowych.

%package utils
Summary:	Dumping and verifying iso9660 images
Summary(pl.UTF-8):	Zrzucanie i weryfikacja obrazów iso9660
Group:		Applications/System

%description utils
Utility programs for dumping and verifying iso9660 images.

%description utils -l pl.UTF-8
Narzędzia do zrzucania i weryfikacji obrazów iso9660.

%package mkisofs
Summary:	Creates an ISO9660 filesystem image
Summary(de.UTF-8):	Erstellt ein Dateisystem-Abbild nach ISO9660
Summary(es.UTF-8):	Crea una imagen de un sistema de archivos ISO9660
Summary(fr.UTF-8):	Crée un image système de fichiers ISO9660
Summary(pl.UTF-8):	Tworzy obraz systemu plików ISO9660
Summary(pt_BR.UTF-8):	Cria uma imagem de um sistema de arquivos ISO9660
Summary(ru.UTF-8):	Создает образ файловой системы ISO9660
Summary(tr.UTF-8):	ISO9660 dosya sistemi kopyası oluşturur
Summary(uk.UTF-8):	Створює образ файлової системи ISO9660
Group:		Applications/System
Provides:	mkisofs = %{epoch}:%{version}-%{release}
Obsoletes:	mkisofs

%description mkisofs
This is the mkisofs package. It is used to create ISO 9660 file system
images for creating CD-ROMs.

%description mkisofs -l es.UTF-8
Este es el paquete mkisofs. Se le usa para crear imágenes de sistema
de archivos ISO 9660 en la creación de CD-ROMs. Ahora incluye soporte
para hacer CD-ROMs de boot "El Torito".

%description mkisofs -l pl.UTF-8
To jest pakiet mkisofs. Jest on używany do tworzenia obrazów systemów
plików ISO9660 potrzebnych do tworzenia płyt CD-ROM.

%description mkisofs -l pt_BR.UTF-8
Este é o pacote mkisofs. Ele é usado para criar imagens de sistema de
arquivos ISO 9660 para criação de CD-ROMs. Agora inclui suporte para
fazer CD-ROMs de boot "El Torito".

%description mkisofs -l ru.UTF-8
Программа mkisofs используется для подготовки мастер-диска, т.е. она
генерирует файловую систему ISO9660. Mkisofs делает снимок заданного
дерева каталогов и генерирует бинарный образ этого дерева, который
соответствует файловой системе ISO9660, записываемой на блочное
устройство. Mkisofs используется для записи CD-ROM'ов и включает
поддержку создания загружаемых El Torito CD-ROM'ов.

%description mkisofs -l uk.UTF-8
Програма mkisofs використовується для підготовки мастер-диску, вона
генерує файлову систему ISO9660. Mkisofs робить знімок заданого дерева
каталогів та генерує бінарный образ цього дерева, який відповідає
файловій системі ISO9660, записуваній на блочний пристрій. Mkisofs
використовується для запису CD-ROM'ів і має підтримку створення
завантажуваних El Torito CD-ROM'ів.

%package btcflash
Summary:	BTC CD/DVD reader/writer firmware updater
Summary(pl.UTF-8):	Program do uaktualniania firmware'u czytników/nagrywarek CD/DVD BTC
Group:		Applications/System

%description btcflash
BTC CD/DVD reader/writer firmware updater.

%description btcflash -l pl.UTF-8
Program do uaktualniania firmware'u czytników/nagrywarek CD/DVD firmy
BTC.

%prep
%setup -q
chmod -R u+rw -R .
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Remove profiled make files
%{__rm} -v $(find . -name '*_p.mk')

cp -p /usr/share/automake/config.* conf

# kill annoying beep and sleep
%{__sed} -i -e 's/^__gmake_warn.*//g' RULES/mk-gmake.id

%{__sed} -i -e "s/-o \$(INSUSR) -g \$(INSGRP)//g" RULES/rules.prg
%{__sed} -i -e 's#/\*.*\*/##g' autoconf/xconfig.h.in

%{__sed} -i -e 's/^\(INSDIR=.*\)lib$/\1%{_lib}/g' lib*/*.mk
%{__sed} -i -e 's/lib\/siconv/%{_lib}\/siconv/g' \
	libsiconv/{sic_nls.c,*/*.mk} mkisofs/{diag/isoinfo.c,mkisofs.c}

%{__sed} -i -e 's#/usr/bin/gm4#%{_bindir}/m4#g' autoconf/autoconf

cd autoconf
install -d m4
%{__mv} acgeneral.m4 acspecific.m4 autoheader.m4 acoldnames.m4 autoconf.m4 m4
%{__mv} aclocal.m4 acinclude.m4

for a in acgeneral.m4 acspecific.m4 autoheader.m4 acoldnames.m4 autoconf.m4; do
	:> $a
done

# extract only needed functions
sed -n -e '/AC_TRY_COMPILE2/,/dnl ###/ { s/AC_LANG/_AC_LANG/; p }' \
	-e '/AC_RCHECK_FUNC/,/dnl ### Checking compiler/ { s/AC_LANG/_AC_LANG/; p }' \
	-e '/AC_INCL_CHECK_TYPE/,/dnl ###/p' m4/acgeneral.m4 >> acinclude.m4
sed -n -e '/CONFIG_RMTCALL/,/^])/p' m4/acspecific.m4 >> acinclude.m4

%build
cd autoconf
%{__aclocal} -I .
%{__autoconf}
cd ../cdda2wav
%{__autoconf}
cd ..
%{__make} -j1 \
	PARCH=%{parch} \
	O_ARCH=%{_target_os} \
	CCOM=gcc \
	CC="%{__cc}" \
	LDCC="%{__cc}" \
	COPTOPT="%{rpmcflags}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS1="%{rpmldflags}" \
	XEXEEXT=

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	PARCH=%{parch} \
	O_ARCH=%{_target_os} \
	CCOM=gcc \
	DEFINSUMASK=002 \
	DEFINSMODEF=644 \
	DEFINSMODEX=755 \
	INS_BASE=%{_prefix} \
	XEXEEXT= \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/{mkisofs,rscsi,cdrecord,cdda2wav,libparanoia}
# schily build system is not packaged
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man5/makefiles.5*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man5/makerules.5*
# belong to glibc/POSIX man pages
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/{error,fexecve,fnmatch,fprintf,getline,printf,sprintf,strlen}.3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AN-* CDDL.Schily.txt COPYING Changelog README make_diskt@2.sh cdrecord/README.{ATAPI,DiskT@2,WORM,audio,cdplus,cdtext,cdrw,clone,copy,multi,parallel,raw,rscsi,sony,verify} cdrecord/{LICENSE,cdrecord.dfl} doc/cdrecord.ps
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cdrecord.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rscsi.conf
%attr(755,root,root) %{_bindir}/cdrecord
%attr(755,root,root) %{_bindir}/scgcheck
%attr(755,root,root) %{_bindir}/scgskeleton
%attr(755,root,root) %{_sbindir}/rscsi
%{_mandir}/man1/cdrecord.1*
%{_mandir}/man1/rscsi.1*
%{_mandir}/man1/scgcheck.1*
%{_mandir}/man1/scgskeleton.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcdrdeflt.a
%{_libdir}/libdeflt.a
%{_libdir}/libedc_ecc.a
%{_libdir}/libedc_ecc_dec.a
%{_libdir}/libfile.a
%{_libdir}/libfind.a
%{_libdir}/libhfs.a
%{_libdir}/libmdigest.a
%{_libdir}/libparanoia.a
%{_libdir}/librscg.a
%{_libdir}/libscg.a
%{_libdir}/libscgcmd.a
%{_libdir}/libschily.a
%{_libdir}/libsiconv.a
%{_includedir}/scg
%{_includedir}/schily
%{_mandir}/man3/absfpath.3*
%{_mandir}/man3/absnpath.3*
%{_mandir}/man3/abspath.3*
%{_mandir}/man3/astoi.3*
%{_mandir}/man3/astol.3*
%{_mandir}/man3/breakline.3*
%{_mandir}/man3/comerr.3*
%{_mandir}/man3/comerrno.3*
%{_mandir}/man3/errmsg.3*
%{_mandir}/man3/errmsgno.3*
%{_mandir}/man3/fdown.3*
%{_mandir}/man3/fdup.3*
%{_mandir}/man3/fexecl.3*
%{_mandir}/man3/fexecle.3*
%{_mandir}/man3/fexecv.3*
%{_mandir}/man3/fgetline.3*
%{_mandir}/man3/file_raise.3*
%{_mandir}/man3/fileclose.3*
%{_mandir}/man3/fileluopen.3*
%{_mandir}/man3/fileopen.3*
%{_mandir}/man3/filepos.3*
%{_mandir}/man3/fileread.3*
%{_mandir}/man3/filereopen.3*
%{_mandir}/man3/fileseek.3*
%{_mandir}/man3/filesize.3*
%{_mandir}/man3/filestat.3*
%{_mandir}/man3/filewrite.3*
%{_mandir}/man3/findline.3*
%{_mandir}/man3/flush.3*
%{_mandir}/man3/format.3*
%{_mandir}/man3/fpipe.3*
%{_mandir}/man3/getallargs.3*
%{_mandir}/man3/getargs.3*
%{_mandir}/man3/geterrno.3*
%{_mandir}/man3/getfiles.3*
%{_mandir}/man3/handlecond.3*
%{_mandir}/man3/movebytes.3*
%{_mandir}/man3/ofindline.3*
%{_mandir}/man3/patcompile.3*
%{_mandir}/man3/patmatch.3*
%{_mandir}/man3/peekc.3*
%{_mandir}/man3/raisecond.3*
%{_mandir}/man3/resolvefpath.3*
%{_mandir}/man3/resolvenpath.3*
%{_mandir}/man3/resolvepath.3*
%{_mandir}/man3/spawnl.3*
%{_mandir}/man3/spawnv.3*
%{_mandir}/man3/strcatl.3*
%{_mandir}/man3/streql.3*

%files cdda2wav
%defattr(644,root,root,755)
%doc cdda2wav/{FAQ,Frontends,HOWTOUSE,OtherProgs,README,THANKS,TODO,cdda2mp3.new,cdda_links,pitchplay,readmult,tracknames.pl,tracknames.txt}
%attr(755,root,root) %{_bindir}/cdda2wav
%attr(755,root,root) %{_bindir}/cdda2mp3
%attr(755,root,root) %{_bindir}/cdda2ogg
%{_mandir}/man1/cdda2wav.1*
%{_mandir}/man1/cdda2mp3.1*
%{_mandir}/man1/cdda2ogg.1*

%files readcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/readcd
%{_mandir}/man1/readcd.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/devdump
%attr(755,root,root) %{_bindir}/isodebug
%attr(755,root,root) %{_bindir}/isoinfo
%attr(755,root,root) %{_bindir}/isovfy
%attr(755,root,root) %{_bindir}/isodump
%{_mandir}/man8/isoinfo.8*
%{_mandir}/man8/devdump.8*
%{_mandir}/man8/isovfy.8*
%{_mandir}/man8/isodump.8*
%{_mandir}/man8/isodebug.8*

%files mkisofs
%defattr(644,root,root,755)
%doc README.mkisofs mkisofs/README mkisofs/README.{compression,eltorito,graft_dirs,hfs_boot,hfs_magic,hide,joliet,mkhybrid,prep_boot,rootinfo,session,sort,sparcboot}
%attr(755,root,root) %{_bindir}/mkisofs
%attr(755,root,root) %{_bindir}/mkhybrid
%{_libdir}/siconv
%{_mandir}/man8/mkisofs.8*
%{_mandir}/man8/mkhybrid.8*

%files btcflash
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/btcflash
%{_mandir}/man1/btcflash.1*
