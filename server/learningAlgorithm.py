import re
from cStringIO import StringIO
from stemming.porter2 import stem
import string
from sklearn import svm


def normalize(word):
    for c in string.punctuation:
        if c!="-" and c!="_":
            word=word.replace(c," ")
        else:
            word=word.replace(c,"")
            word=re.sub("[\\s|\\d]+"," ",word)
    return stem(word.lower())
ByUs=["abstract","try","use","#oneCharacter","research","learn","you",'#"',"comparison","#_","conclusion","computer","algorithm","see","internet","web","code","tool","api","software","server","references"]

ByUs=[normalize(word) if '#' not in word else word for word in ByUs]
Found=["Client","ABEND:","Abnormal","End","of","Task","ABEND:","Absent","By","Enforced","Net","Deprivation","ABI:","Application","Binary","Interface","-","","ABNF:","Augmented","Backus","Naur","Form","Abstract","Base","Class","Abstract","Type","ACCU:","Association","of","C","and","C++","Users","ACD","Canvas","ACDI:","Asynchronous","Communications","Device","Interface","ACF","NCP:","Advanced","Communication","Function","-","Network","Control","Program","Acrobat","-","","Action","Request","System","ActionScript","-","","Active","Cell","Active","Content","-","","ActiveMovie","ActiveX","Programs","ACT-R","-","","Ada","-","","ADABAS","-","","Adaptiv","Workforce","-","","Adaptive","Server","Enterprise","(ASE)","Ad-Aware","Add-in","-","","Add-on","-","","AdeptXBBS","ADF:","Application","Development","Facility","ADL:","Architecture","Description","Language","Adobe","Acrobat","Adobe","Audition","Adobe","Illustrator","-","","ADP:","Automatic","Data","Processing","Adware","-","","AE:","Action","Evolution","-","","AFC:","Advanced","Communication","Function","-","","AFK","Gaming","After","Dark","Agent","Software","AI:","Artificial","Intelligence","AIGLX:","Accelerated","Indirect","GLX","AIX:","Advanced","Interactive","eXecutive","Algol","Object","Code","Algorithm","Allegro","Library","-","","Aloha","-","","Alpha","Test","Alpha","Version","Alphanumeric","ALSA:","Advanced","Linux","Sound","Architecture","ALTQ:","ALTernate","Queueing","Aluria","Software","AmigaOS","AML:","Astronomical","Markup","Language","Amoeba","Anatomic","P2P","ANDF:","Architecture","Neutral","Distribution","Format","Angel","Operating","System","ANSYS","Anti-Adware","-","","Antique","Software","AOS:","Add","One","and","do","not","Skip","Apache","Apache","HTTP","Server","Apache","Incubator","Apache","Project","Apache","Tomcat","API","Documentation","API:","Application","Programming","Interface","AppleScript","AppleShare","-","","Applet","-","","Application","Application","Framework","Application","Macro","Application","Package","Application","Program","Application","Programmer","Application","Server","-","","Application","Software","Application","Stack","-","","Application","Suite","-","","APSE:","Ada","Programming","Support","Environment","AR","Mid-Tier:","Action","Request","Mid-Tier","AR","System","Administrator","-","","AR","System","Import","AR","System:","Action","Request","System","Architecture","-","","Ardour","ASLR:","Address","Space","Layout","Randomization","ASP:","Active","Server","Pages","ASPack","Assembly","-","","Assembly","Language","Audacity","Authoring","Tool","-","","AutoCAD","AutoDesk","Autodesk","Animator","Autodesk","Inventor","AUTOEXEC.BAT","AutoLISP","Automated","information","system","Automatic","Parallelization","Automatic","Vectorization","Autoresponder","-","","Autosketch","Autotote","Avidemux","Avionics","Software","B2evolution","Backup","Backup","&","Recovery","Backward","Compatible","-","","Baitware","-","","BASH:","Bourne-Again","Shell","BASIC","bBlog","BCNF:","Boyce-Codd","Normal","Form","BCX:","Basic","To","C","Translator","BDS","C:","BD","Software","C","Compiler","Bedroom","Programming","-","","Bells","and","Whistles","Berkely","Software","Design","Bespoke","Software","Beta","Test","Beta","Version","BetBug","BI","software:","Business","Intelligence","Software","Binary","Compatible","-","","Binary","Tree","Binding","Time","-","","Bit","Rot","BitComet","BitLord","BitTorrent","Client","Bloatware","Blog","Client","-","","Blogware","Blue","Martini","Software","BMRT:","Blue","Moon","Rendering","Tools","BNF:","Backus","Naur","Form","-","","BoastMachine","Boehm","Garbage","Collector","Bookmark","Boolean","Boolean","Algebra","Boolean","AND","Boolean","logic","Boolean","OR","Boolean","value","Boost","Library","Bootstrapping","Bot:","RoBOTic","Computer","Ccontrolled","Entity","Bottom-up","Design","Bounds-Checking","Elimination","BRL-CAD","Brute","Force","Programing","BSA:","Business","Software","Alliance","-","","BSD","Daemon","BSD","license:","Berkeley","Software","Distribution","License","BSD/OS","BSD:","Berkeley","Software","Distribution","BSP:","Board","Support","Package","BSS:","Block","Started","by","Symbol","BST:","Binary","Search","Tree","Budget","Range","Bug","Bundled","Software","Business","Software","-","","Byte-Code","Bzip2","C","Programming","Language","C#","C++","CAAD:","Computer","Aided","Architectural","Design","CAD:","Computer","Aided","Design","CADD:","Computer-Aided","Design","and","Drafting","CAE:","Computer-Aided","Engineering","CAID:","Computer-Aided","Industrial","Design","-","","Callback","Call-by-Reference","Call-by-Value","CAM:","Computer-Aided","Manufacturing","CAMA:","Computer","Assisted","Mass","Appraisal","CAR:","Computer-Assisted","Reviewing","Careware","-","","CASE:","Computer","Aided","Software","Engineering","-","","Casting","Variable","CATIA","Cc65","-","","CCEA:","Citrix","Certified","Enterprise","Administrator","-","","CD","Grabber","CD","Ripper","CD/DVD","Authoring","CDDL:","Common","Development","and","Distribution","License","CeCILL:","CEA","CNRS","INRIA","Logiciel","Libre","Cedega","-","","Celestia","Censorware","-","","CFG:","Control","Flow","Graph","-","","CFML:","ColdFusion","Markup","Language","CGI:","Common","Gateway","Interface","cgi-bin","CGI:","Computer","Generated","Imagery","Character","Character","Code","-","","Character","Encoding","Character","Mapping","Character","Repertoire","Character","Set","-","","Charmap:","Character","Map","Checkpoint","Chinook","Checkers","Program","CIF:","Common","Intermediate","Format","CIM:","Common","Information","Model","Citadel","Software","CL:","Common","LISP","Class","Class","Library","Clean","Install","-","","ClearCase","-","","ClearDDTS","-","","ClearQuest","-","","Client","-","","Client-Side","CLISP","Closed","Source","ClosedBSD","Cloud","computing","cmd.exe","CML:","Chemical","Markup","Language","CMM:","Capabilities","Maturity","Model","-","","Coco/R","-","","COCOMO:","Constructive","Cost","Model","Code","Code","Co-op","Code","Generation","Codec:","Compression/Decompression","Coded","Character","Set","CodeView","CodeWarrior","-","","Coding","-","","COE:","Common","Operating","Environment","-","","Cognitive","Architecture","ColdFusion","-","","Collaborative","Software","-","","COM:","Component","Object","Model","-","","Command","-","","Command","Interpreter","Command.com","Commercial","Software","Common","Core","Services","-","","Communications","Software","-","","Compatible","-","","Compiler","Compiler","Bug","Compiler","Directive","Compiler","Optimization","Compiler-Compiler","Componetware:","Component","Software","-","","Computational","Linguistics","Computational","Science","Computer","Animation","Computer","Game","Computer","Graphics","Computer","Science","ConceptBase","Config","Files:","Configuration","Files","CONFIG.SYS","Configuration","-","","Configuration","Management","-","","Constant","Folding","Constant","Propagation","-","","Constraint","Logic","Programming","Constraint","Programming","Constraint","Satisfaction","Content","Management","System","Control","Panel","Cooperative","Multitasking","Copy","Propagation","Copycat","Copyleft","-","","Copyright","Copyright","Infringement","-","","CORC:","CORnell","Compiler","CORE:","Challenge","of","Reverse","Engineering","CosmicOS","Course","Management","System","Crack","Intro","Critical","Section","CRM:","Customer","Relationship","Management","Cron","Cross","Compiler","Crowd","Simulation","CSCI:","Computer","Software","Configuration","Item","-","","CSE:","Common","Subexpression","Elimination","CSV:","Comma","Separated","Values","CUA:","Common","User","Access","-","","Cubase","Custom","Software","Customized","Toolbar","-","","CVS:","Concurrent","Versions","System","-","","Cwiab:","Church","Website","in","a","Box","Cyclomatic","Complexity","Cygwin","Daemon","DAM:","Digital","Asset","Management","DARCS:","David's","Advanced","Revision","Control","System","Data","-","","Data","Architect","Data","Architecture","-","","Data","Cleansing","-","","Data","Conversion","Data","Element","Data","element","definition","Data","Mapping","Data","Migration","-","","Data","Modeling","-","","Data","Processing","-","","Data","Scrubbing","-","","Data","Structure","Data","Transformation","Database","Administration","Database","Model","Database","Normalization","Database","Object","Database","Query","Language","Database","Server","Datalog","Dating","Software","DB/DC:","Database/Data","Communications","DB:","Database","-","","DB2:","DataBase","2","-","","DBA:","Database","Administrator","DBase","DBCS:","Double-Byte","Character","Set","DBI:","DataBase","Interface","for","Perl","DBMS:","Database","Management","Ssystem","-","","Dbx","Debugger","DCL:","Data","Control","Language","DCOM:","Distributed","Component","Object","Model","DDD:","Data","Display","Debugger","DDL:","Data","Definition","Language","DDMS:","Distributed","Database","Management","System","DDT:","Dynamic","Debugging","Technique","Dead","Code","-","","Dead","code","Elimination","Debug","Monitor","Debugger","Decompiler","Deflate","Algorithm","Defragment","-","","Dehardwarization","-","","Delphi","Demo:","Demostration","Version","Demoware","Deprecated","Software","Der","Dirigent","Design","Compiler","-","","DeskScan","DesktopBSD","Dev-C++","Device","Driver","DGCA","-","","DIB:","Device-Independent","Bitmap","-","","Digial","pen","Digital","Paper","-","","Digital","Wallet","-","","DirectX","-","","Disassembly","Disassembler","Distcc","Distiller","Distributed","Computing","-","","Distributed","Database","Distribution","Software","DJGPP","DKBTrace","-","","DLL","Hell","DLL:","Dynamic-Link","Library","DM:","Data","Mart","-","","DM:","Data","Mining","DML:","Data","Manipulation","Language","DMX:","Data","Mining","Extensions","Doc-O-Matic","Document!","X","-","","DOMi:","DOM","Inspector","Donateware","-","","DOOM","Doom","WAD","DOS:","Disk","Operating","System","DotGNU","DotNetNuke","Doxygen","Drawing","Program","DRDA:","Distributed","Relational","Database","Architecture","Dreamweaver","-","","Dribbleware","-","","Driver","Wrapper","Drupal","DSI:","Delivered","Source","Instruction","DSL:","Domain-Specific","Language","DSSI:","Disposable","Soft","Synth","Interface","DW:","Data","Warehouse","EBNF:","Extended","Backus","Naur","form","ECM:","Enterprise","Content","Management","Editor","-","","EFence:","Electric","Fence","EFSM:","Extended","Finite","State","Machine","Model","EGCS:","Experimental/Enhanced","GNU","Compiler","System","EIAS:","Electric","Image","Animation","System","Emacs","Emacs","LISP","Emulation","Emulation","Mode","-","","Emulator","Enterprise","Software","Enterprise","Software","Architecture","Entropy","-","","ESC/Java:","Extended","Static","Checker","for","Java","Etnus","TotalView","-","","Evaluation","Strategy","Exec","Shield","-","","Extended","ASCII","-","","EXtensible","Markup","Language","(XML)","External","Command","-","","Extreme","Programming","-","","EZ","Publish","FAB:","FORTRAN","Assembly","Program","FASM:","Flat","Assembler","FAST:","Federation","Against","Software","Theft","FastCAD","-","","FAT:","File","Allocation","Table","-","","Fat","Binary","Fetch-and-add","CPU","instruction","Fibonacci","Number","Program","Fibonacci","Numbers","Fifth-Generation","Programming","Language","FileMaker","Pro","Filename","Extension","Fiora","FireFox","Firmware","First","Generation","Programming","Language","FLAC:","Free","Lossless","Audio","Codec","Flex","Lexical","Analyser","Generator","FMV:","Full","Motion","Video","FOP:","Formatting","Objects","Processor","FORTRAN","Forward","Compatible","Fourier","Transform","Fourth-Generation","Language","-","","FPA:","Function","Point","Analysis","-","","Free","Software","-","","Free","Software","License","FreeBASIC","FreeBSD","FreeDoom","-","","FreeSBIE","FreeTDS","FrontPage","FSF:","Free","Software","Foundation","FSM:","Finite","State","Machine","FSML:","Financial","Services","Markup","Language","FTP","Client","Functional","Programming","Functional","Programming","Language","GA:","Global","Arrays","-","","GAMS:","General","Algebraic","Modeling","System","-","","Gas:","GNU","Assembler","GCA","GCC:","GNU","Compiler","Collection","-","","GCJ:","GNU","Compiler","for","Java","GDB:","GNU","Debugger","GDL:","GNU","Data","Language","GNOME","Display","Manager","Geeklog","Generic","Software","GeoGebra","Geronimo","Application","Server","gFTP","GHC:","Glasgow","Haskell","Compiler","Ghost:","General","Hardware-Oriented","Software","Transfer","GIFT:","GNU","Image","Finding","Tool","GIMP:","GNU","Image","Manipulation","Program","-","","glibc:","GNU","C","Library","GLPK:","GNU","Linear","Programming","Kit","-","","Glueware","Gmail","Drive","GML:","Generalized","Markup","Language","GNAT:","GNU","NYU","Ada","Translator","GNAVI","-","","GNOME:","GNU","Network","Object","Model","Environment","GNU","Arch","GNU","Aspell","GNU","Build","System","GNU","General","Public","License","GNU","Hurd","GNU","Mach","GNU","MDK:","GNU","MIX","Development","Kit","GNU","Readline","GNU","Robots","GNU","Savannah","GNU","Screen","GNU","TEXMACS","GNU","Toolchain","GNU/kFreeBSD","GNU/Linux","GNU/NetBSD","GNU:","Gnu's","Not","UNIX","-","","GNUstep","Goto","GPL:","General","Public","License","GPL:","General","Purpose","Language","GPS:","GNAT","Programming","Studio","Greenware","Greyware","-","","Groupware","GSL:","GNU","Scientific","Library","GTK+:","GIMP","Toolkit","GTK-Qt","GUI:","Graphical","User","Interface","Guiltware","GVN:","Global","value","numbering","GW","Basic","Gzip:","GNU","zip","Handwriting","Recognition","Haskell","Programming","Language","Helper","Applications","Heterogeneous","System","Hex","editor","High-Level","Language","HLA:","High","Level","Architecture","-","","HLA:","High","Level","Assembly","HMP:","Hybrid","Multiprocessing","Hoard","Memory","Allocator","Homogeneous","System","Horizontal","Software","-","","HotHTML","HSQLDB","HTML","Editor","HTML-Kit","Hydrogen","Software","HyperCard","-","","Hypermedia","HyperTalk","IBALANCE","IDE:","Integrated","Development","Environment","-","","I-DEAS:","Integrated-Design","Engineering","Analysis","Software","IDMS:","Integrated","Database","Management","System","IEEE","829-1998","-","","IGS:","Interactive","Geometry","Software","-","","IIS:","Internet","Information","Server","IM:","Identity","Management","ING:","International","Network","of","Crackers","Ingres","INI","File:","Initialization","File","Inline","Expansion","Instruction","-","","Instruction","Scheduling","Instruction","Selection","Instruction","Set","Insure++","Integrated","Software","Package","Integration","Testing","Intelligent","Device","Management","IntelliJ","IDEA","Interchangeability","Interface","Interface","Encapsulation","Interface","Standard","Internal","Command","-","","Interpreter","Program","Interprocedural","Optimization","Inverse","mapping","Iprism","IR:","Information","Retrieval","IRC","Bot:","Internet","Relay","Chat","Bot","ISA:","Instruction","Set","Architecture","IT","Management:","Information","Technology","Management","IT:","Information","Technology","ITS:","Incompatible","Time-Sharing","System","IZArc","J2EE:","Java","2","Platform,","Enterprise","Edition","JACK","Audio","Connection","Kit","JADE","Programming","Language","Jakarta","Project","Java","-","","Java","Beans","Java","Bytecode","Java","EE:","Java","Platform,","Enterprise","Edition","-","","Java","Programming","Language","JavaCC:","Java","Compiler","Compiler","Javadoc","JavaScript","Jbuilder","JCP:","Java","Community","Process","JDBC:","Java","Database","Connectivity","JHTML:","Java","HTML","JMS:","Java","Message","Service","-","","JMX:","Java","Management","Extensions","-","","JOGL:","Java","OpenGL","JOLIX","Joomla!","JRT","JSR:","Java","Specification","Request","JSwat","JuK","Jump","Command","Jump","Threading","JVM:","Java","Virtual","Machine","Kazaa","Lite","K++","Kazaa","Lite","Resurrection","Kazaa","Lite","Revolution","Kazaa","or","Kazzaa","K-Lite:","Kazaa","Lite","Karma","KDbg","-","","KDE:","K","Desktop","Environment","KDEAP:","KDE","Accessibility","Project","KDM:","KDE","Display","Manager","Kernel","Kernel",
"Mode","Keyboard","Macro","Keyboard","Mapping","Keychan:","Key","Changer","Keygen:","Key","Generator","KHTML","Killer","App:","Killer","Application","KIS:","Knowbot","Information","Service","-","","K-Meleon","-","","Knowbot:","Knowleage","Robot","KOMPAS-3D","Kpackage","Kparts","Ktorrent","KVCD","Kylix","LADSPA:","Linux","Audio","Developers","Simple","Plugin","API","LAMIP:","Linux","Audio","Multiple","Interface","Player","LAMP:","Linux,","Apache,","MySQL","and","Perl/PHP/Python","LAN","Server","Lattice","C","Lava","Programming","Language","Lazy","Evaluation","LCC:","Local","C","Compiler","Legacy","System","LGPL:","Lesser","General","Public","License","-","","LHA","Libmp3splt","Libre","Software","LightWave","Linker","Linoleum","Programming","Language","Lint","Programming","Tool","Linux","Linux","kernel","Linux","PC","LIS:","Laboratory","Information","System","LISP","Programming","Language","Live","Variable","Analysis","LiveCD","LiveDistro","LMS:","Learning","Management","System","LNO:","Loop","Nest","Optimization","Loader","Program","Locator","Program","Logic","Programming","Loop","Fission","Loop","Fusion","Loop","Interchange","Loop","Inversion","-","","Loop","Optimization","Loop","Splitting","Loop","Tiling","Loop","Transformation","Loop","Unswitching","Loop","Unwinding","Loop-Invariant","Code","Motion","Low-Level","Language","LSM:","Linux","Software","Map","LURCH","LWP:","Light-Weight","Process","LZO:","Lempel-Ziv-Oberhumer","Mac","OS","X","-","","Mac","OS:","Macintosh","Operating","System","Machine","Code","Machine","Code","Instruction","Machine","Language","-","","Macro","Macro","Language","Macro-instruction","Macromedia","Flash","MacsBug:","Motorola","Advanced","Computer","Systems","Debugger","Magnolia","CMS","MakeRefMovie","Mambo","CMS","MASM:","Microsoft","Macro","Assembler","MCAD:","Microsoft","Certified","Application","Developer","MCDBA:","Microsoft","Certified","Database","Administrator","MCDST:","Microsoft","Certified","Desktop","Support","Technician","MCP:","Microsoft","Certified","Professional","MCSA:","Microsoft","Certified","Systems","Administrator","MCSD:","Microsoft","Certified","Solution","Developer","MCSE:","Microsoft","Certified","Systems","Engineer","MCT:","Microsoft","Certified","Trainer","MDX:","Multidimensional","Expressions","Media","Cleaner","Pro","Memory","Management","Memwatch","Metadata","MicroBSD","Microcode","Microinstruction:","Micro","code","Instruction","Microkernel","Micro-programming","Microsoft",".Net","Microsoft",".Net","Framework","Microsoft","Access","Microsoft","SQL","Server","Microsoft","Systems","Management","Server","Microsoft","Visual","Studio","Debugger","Microsoft","Windows","-","","MicroStation","Middleware","MinGW","Developer","Studio","MinGW:","Minimalist","GNU","for","Windows","Minix","MIS:","Management","Information","systems","MISRA","C","MISRA:","Motor","Industry","Software","Reliability","Association","MIT","License:","Massachusetts","Institute","of","Technology","License","Module","-","","Monad","Monotone","Moodle","MOS:","Microsoft","Office","Specialist","Mosaic","Moto","Programming","Language","-","","MOV:","Merchant","of","Venice","-","","Mozbot","Mozilla","Mozilla","Application","Object","Model","(AOM)","Mozilla","Firefox","Mozilla","Public","License","Mp3splt","Mp3splt-gtk","MPS:","Memory","Pool","System","MS-DOS:","MicroSoft","Disk","Operating","System","mSQL:","Mini","SQL","mSQL-JDBC","MSYS:","Minimal","SYStem","MUI:","Magic","User","Interface","Multiple","Perspective","Software","Development","Multiprocessing","Multitasking","Multithreading","MusE","MySQL","Mystic","BBS","Nagware","Name","Binding","Nanika","NanoCAD","NASM:","Netwide","Assembler","Natural","Docs","Natural","Language","NetBSD","News","Aggregator","NF:","Normal","Form","NLP:","Natural","Language","Processing","No-CD","Crack","Nodezilla","Non-code","resource","Non-compressed","sound","data","Nonlinear","Programming","-","","Non-Printable","Character","Non-Proprietary","Software","Nonrelocatable","Block","-","","NonStop","SQL","Nonvolatile","Register","-","","Normalization","in","Database","Novell","ZENworks","NPL:","Netscape","Public","License","NuCalc","Numerical","Analysis","-","","OATH:","Object-Oriented","Abstract","Type","Hierarchy","-","","Object","-","","Object","code","-","","Object","Model","Object","Database","Object","Pool","Object-SQL","Mapping","Objectworks","OD390","ODA:","Open","Document","Architecture","ODBC:","Open","Database","Connectivity","ODBMS:","Object","Database","Management","System","ODNT:","Object","Desktop","Network","O.K.I.:","Open","Knowledge","Initiative","OLAP:","Online","Analytical","Processing","OLE:","Object","Linking","and","Embedding","OLTP:","Online","Transaction","Processing","(OLTP)","OMG:","Object","Management","Group","OmniPage","Professional","OO","Language:","Object-Oriented","Language","OODBMS:","Object","Oriented","Database","Management","System","-","","OOP:","Object-Oriented","Programming","Open","Group","-","","OPEN","LOOK","Open","Outsourcing","Open","Source","Open","Source","Movement","Open64","-","","OpenBSD","OpenBSM","OpenC++","OpenDoc","-","","OpenGL:","Open","Graphics","Library","OpenKore","OpenNTPD","OpenROAD:","Open","Rapid","Object","Application","Development","OpenSolaris","Open-Source","License","OpenTracker","Operating","Environment","-","","OPS5:","Official","Production","System","Oracle","Database","-","","ORB:","Object","Request","Broker","ORD:","Object-Relational","Database","ORDBMS:","Object-Relational","Database","Management","System","-","","OS/2:","Operating","System/2","OS:","Operating","System","OSD:","Open","Source","Definition","OSF:","Open","Software","Foundation","OSI:","Open","Source","Initiative","OSID:","Open","Service","Interface","Definition","OSS/J:","OSS","Through","Java","OSS:","Open","Sound","System","OSS:","Open-Source","Software","Outliner","-","","p7zip","Packaged","Software","Page","Recognition","Paint","Program","Parallel","Algorithm","Parallel","Compiler","Parallel","Computing","-","","Parallel","Port","Parallel","Processing","-","","Parallel","Terraced","Scan","Parser","Program","Parsing","Process","Partial","Evaluation","Pascal","programming","Language","Patch","-","","Pattern","Matching","Payware","PC","Weenies","PCBoard","PC-BSD","PC-DOS:","Personal","Computer-Disk","Operating","System","PCL:","Printer","Control","Language","PCMS:","Platform","Content","Management","System","PDF:","Portable","Document","Format","PDL:","Page","Description","Language","PEEK","and","POKE","Peephole","Optimization","People","Aggregator","Per","Seat","Perl:","Practical","Extraction","and","Reporting","Language","PHP","Hypertext","Preprocessor","PHPEdit","Physalis","PID:","Process","Identifier","Piracy","PKZIP:","Phil","Katz's","ZIP","Planner","Programming","Language","Plugin","or","Plug-In","Podcatcher","Polyfont","Recognition","-","","Portable","Software","POSIX:","Portable","Operating","System","Interface","Postgres","PostScript","POV-Ray:","Persistence","of","Vision","Raytracer","PowerAnimator","PowerArchiver","PowerBASIC","PPM:","Project","Portfolio","Management","PRE:","Partial","Redundancy","Elimination","Preemptive","Pre-Emptive","Multitasking","Preprocessor","Priority","Inversion","Pro","Tools","Procedural","Language","Procedure","Procedure","Programing","Processor-Independent","Software","Processor-Specific","Software","Profiler","Program","-","","Programming","Language","Programming","Macro","Programming","Tool","Prolog","Proprietary","Software","PSE:","Problem","Solving","Environment","Pseudonymous","Remailer","Public-Domain","Software","PUP:","Potentially","Unwanted","Program","Purify","Memory","Debugger","PWB","Shell","PyGTK","PyQt","Python","QB:","QuickBASIC","Qbasic","Qcad","QTW:","QuickTime","for","Windows","Query","Language","Query","Optimizer","Query","Plan","QuickTime","QVCS","R","Programming","Language","Racter:","Raconteur","Rainlender","RAR:","Roshal","Archive","RDBMS:","Relational","Database","Management","System","RealSky","Recursive","Redundant","Code","Reentrant","Refactoring","Register","Allocation","Register","Spilling","Regression","Testing","Relational","Database","Relational","Model","Rematerialization","Remote","Control","Software","Renegade","BBS","Report","Writer","Repository","Open","Service","Interface","Definition","Revision","Control","Revision","Control","System","Rewind","RISC","iX","RISC","OS:","Reduced","Instruction","Set","Computer","Operating","System","RKWard","ROBODoc","Robustness","ROFUG:","Romanian","FreeBSD","Users","Group","RosAsm","Rosegarden","Routine","Rpcdump","rsh:","Remote","Shell","Protocol","RTM:","Release","to","Manufacturing","Rtorrent","RTOS:","Real-Time","Operating","System","RTSC:","Read","the","Source","Code","Ruby","Programming","Language","Runtime","Runtime","Environment","Runtime","Error","Runtime","Library","RUP:","Rational","Unified","Process","Rzip","S","Programming","Language","S/W:","Software","SAA:","Systems","Application","Architecture","Sandbox","Sandwich","Test","SAPI:","Scheduling","Application","Programming","Interface","SAPI:","Speech","Application","Programming","Interface","SCADA:","Supervisory","Control","and","Data","Acquisition","SCANDISK","SCCS:","Source","Code","Control","System","Scientific","Computing","SCM:","Software","Configuration","Management","SCM:","Source","Configuration","Management","Screen","Scraper","ScreenCam","Screencast","Script","Scripting","Languages","SDD:","Software","Description","Database","SDK:","Software","Development","Kit","SDL:","Simple","DirectMedia","Layer","SDLC:","Systems","Development","Life","Cycle","SDML:","Signed","Document","Markup","Language","SDR:","Software-Defined","Radio","SE:","Software","Engineer","-","","Seahorse","Search","Engine","Search","Service","Second","Generation","Language","Second-System","Effect","Security-Enhanced","Linux","SEI:","Software","Engineering","Institute","Self-Extracting","File","SEQUEL:","Structured","English","Query","Language","Server","Application","Service","Oriented","Analysis","SP:","Service","pack","SFA:","Sales","Force","Automation","SGML","Application","SGML:","Standard","Generalized","Markup","Language","Shareaza","Shareware","-","","Shelfware","Shell","Shockwave","Shoutcast","SIGGRAPH:","Special","Interest","Group","in","Graphics","SIIA:","Software","&","Information","Industry","Association","SIT:","System","Integration","Testing","SLOC:","Source","Lines","of","Code","Smalltalk","SOA:","Service-Oriented","Architecture","SOAD:","Service-Oriented","Analysis","and","Design","SOAR","Cognitive","Architecture","Social","Software","SoftICE","Softimage|XSI","Software","Software","Agent","-","","Software","Architecture","Software","Audit","Software","Blacklist","-","","Software","Cracking","Software","Engineering","Software","Entropy","Software","Environment","Software","Generic","Software","Genre","Software","Hoarding","-","","Software","License","Software","Licensing","Software","Life-Cycle","Software","Metric","Software","Package","Software","Pipelining","Software","Piracy","Software","Project","Life","Cycle","Software","Rot","-","","Software","Sampler","-","","Software","Suite","Software","Theft","Software","Tool","SoftwareValet","Source","Code","Source","Code","Repository","Source","Language","Source","Program","SourceForge","SOX","Unix","SoX:","Sound","eXchange","Sparse","Conditional","Constant","Propagation","Spell","Checker","Spider-Man","Cartoon","Maker","Spiral","Model","SPOF:","Single","Point","of","Failure","Spreadsheet","Spreadsheet","Applications","Sproc:","Stored","Procedure","SQL:","Structured","Query","Language","SQLite","Squeez","Utility","Squish","of","FidoNet","SR:","Service","Release","Srvany","SSA:","Static","Single","Assignment","Form","SSADM:","Structured","Systems","Analysis","and","Design","Method","Stack","of","Data","Structure","Startup","Code","Static","Class","Static","Code","Analysis","Static","Library","STL:","Standard","Template","Library","Strength","Reduction","String","Intern","Pool","Structured","Analysis","Structured","Design","Structured","Programming","StuffIt","Expander","Subversion","Subweb","-","","SuperCollider","Programming","Language","SVK","Sweep","Software","Sybase","SQL","Server","Symbolic","Inference","Syntax","-","","Sysadmin:","System","Administrator","System","Call","System","Integrator","System","Resource","System","Software","Systems","Administration","Systems","Analysis","Systems","Management","-","","Systems","Program","Systems","Programmer","Tag","-","","Tape","Library","-","","Task","Scheduling","TASM:","Turbo","Assembler","Telegard","Telelogic","SYNERGY","TenDRA","Compiler","Terragen","Third","Generation","Language","Three","Tier","Architecture","Three","Tier","Model","Time-Sharing","TinyOS","Top-Down","Design","TOS:","Tape","Operating","System","TOS:","The","Operating","System","Trace","Scheduling","Trial","Software","Trigger","-","","TrueSpace","TrueType","TrustedBSD","TTA:","True","Audio","TUGZip","Turbo","BASIC","Turbo","C","Turbo","C++","Turbo","Pascal","Turbo","Software","Tutorial","TwinText","UAT:","User","Acceptance","Testing","UIT:","User","Interface","Toolkit","Ultrix","UML","tool:","Unified","Modeling","Language","tool","UML:","Unified","Modeling","Language","Unix","Unreachable","Code","Upgrade","Ups","Debugger","Upward","Compatible","USG","Unix:","Unix","Support","Group","User","Interface","Utility","Computing","Utility","Program","Valgrind","Vaporware","VB:","Virtual","Basic","Vbcc","VBScript:","Virtual","Basic","Script","VBScript:","Visual","Basic","Script","Edition","Veronica:","Very","Easy","Rodent-Oriented","Net-Wide","Index","to","Computer","Archives","Vertical","Software","Video","Game","Viewer","Program","VirtualGL:","Virtual","Graphics","Library","Visual","C++","VisualKore","-","","VMS:","Virtual","Memory","System","VRML:","Virtual","Reality","Modeling","Language","W2K:","Windows","2000","WAMP:","Microsoft","Windows,","Apache,","MySQL","and","Perl/PHP/Python","Warez","Watchdog","Event","Log","Waterfall","Model","Web","Authoring","Web","Content","Management","System","Web","Page","Web","Portal","Web3D","Consortium","Weblog","Software","Websphere","Widget","Toolkits","Wildcat!","Windbg","Debugger","Window","Me","Windowing","Software","Windowing","System","Windows","1.0","Windows","2.x","Windows","2003","Windows","3.0","Windows","3.1x","Windows","95","Windows","98","Windows","API","Windows","Forms","Windows","NT","Windows","Server","System","Windows","XP","Wine","Software","WinG","Wings","3D","Winny","Program","WinRAR","WinZip","Word","Processing","Word","Processor","Wrapper","Software","WWIV","BBS","WxWidgets","X","Window","System","X.Org","Fundation","X.Org","Server","X/Open","XAD","XCMD:","eXternal","CoMmanD","Xcode","XDBX","XDM:","X","Window","Display","Manager","Xerox","Development","Environment","Xerox","PARC:","Xerox","Palo","Alto","Research","Center","XFCN:","External","Functions","XFree86","X-Men","Cartoon","Maker","XML","Schema","XMLBeans","XMLTerm","XMMS:","X","Multimedia","System","XMMS2:","Cross","Platform","Music","Multiplexing","System","XOTcl","XPCOM:","Cross","Platform","Component","Object","Model","Xterm","XView","Xxgdb","Y","Windows","Yacc:","Yet","Another","Compiler","Compiler","YafRay:","Yet","Another","Free","Raytracer","Z88DK","ZIP","File","Format","ZipGenius","Zipping","Zlib","Torrent","1GL:","First","Generation","Programming","Language","2D","Computer","Graphics","2GL:","Second","Generation","Language","386BSD","3D","Computer","Graphics","3D","Flash","3D","Studio","Max","3GL:","Third","Generation","Language","4GL:","Fourth-Generation","Language","5GL:","Fifth-Generation","Programming","Language","7-Zip"]

Found=[normalize(word) if '#' not in word else word for word in Found]
def ToVS(text):
    VS=dict()
    text=text.lower()
    
    VS["#!"]=len(re.findall("!",text))
    VS["#?"]=len(re.findall("\\?",text))
    VS["#()"]=len(re.findall("\\(|\\)",text))
    VS["#numbers"]=len(re.findall("\\d+",text))
    VS["##"]=len(re.findall("#",text))
    VS["#{}"]=len(re.findall("\\{|\\}",text))
    VS["#[]"]=len(re.findall("\\[|\\]",text))
    VS["#comparison"]=len(re.findall("<|>|=",text))
    VS['#"']=len(re.findall('"',text))
    VS['#math']=len(re.findall('\\+|\\-|\\*|\\/',text))
    VS['#_']=len(re.findall('_',text))
    VS['#oneCharacter']=0
    for c in string.punctuation:
        if c!="-" and c!="_":
            text=text.replace(c," ")
        else:
            text=text.replace(c,"")
    text=re.sub("[\\s|\\d]+"," ",text)
    text=filter(lambda x: x in string.printable, text)
    for w in text.split(" "):
        word=stem(w)
        if word!="":
            if len(word)==1:
                VS["#oneCharacter"]+=1
            elif VS.has_key(word):
                VS[word]+=1
            else:
                VS[word]=1
    return VS

def MapToEvalVS(bag):
    v=[]
    total=0
    for w in bag:
        total+=bag[w];
    for w in ByUs+Found:
        if(bag.has_key(w) and total!=0):
            v.append(bag[w]*1.0/total)
        else:
            v.append(0)
    return v;

def learn(cat1,cat2,cat3):
    X = []
    Y = []
    for d in cat1:
        X.append(MapToEvalVS(d));
        Y.append(0)
    for d in cat1:
        X.append(MapToEvalVS(d));
        Y.append(1)
    for d in cat3:
        X.append(MapToEvalVS(d));
        Y.append(2)
    clf = svm.SVC()
    clf.fit(X, Y)
    return clf

def predict(learner,doc):
    return learner.predict(MapToEvalVS(ToVS(doc)))
