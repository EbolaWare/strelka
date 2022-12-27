from pathlib import Path
from unittest import TestCase, mock

from strelka.scanners.scan_elf import ScanElf as ScanUnderTest
from strelka.tests import run_test_scan


def test_scan_elf(mocker):
    """
    Pass: Sample event matches output of scanner.
    Failure: Unable to load file or sample event fails to match.
    """

    test_scan_event = {
        "elapsed": mock.ANY,
        "flags": [],
        "total": {
            "libraries": 1,
            "relocations": 9,
            "sections": 31,
            "segments": 13,
            "symbols": 43,
        },
        "nx": True,
        "pie": True,
        "header": {
            "endianness": "LSB",
            "entry_point": 4192,
            "file": {"type": "DYNAMIC", "version": "CURRENT"},
            "flags": {
                "arm": [],
                "hexagon": [],
                "mips": [],
                "ppc64": [],
                "processor": 0,
            },
            "identity": {
                "class": "CLASS64",
                "data": "LSB",
                "os_abi": "SYSTEMV",
                "version": "CURRENT",
            },
            "machine": "x86_64",
            "size": 64,
        },
        "interpreter": "/lib64/ld-linux-x86-64.so.2",
        "relocations": [
            {
                "address": 15800,
                "info": 0,
                "purpose": "DYNAMIC",
                "size": 64,
                "symbol": "",
                "type": "RELATIVE",
            },
            {
                "address": 15808,
                "info": 0,
                "purpose": "DYNAMIC",
                "size": 64,
                "symbol": "",
                "type": "RELATIVE",
            },
            {
                "address": 16392,
                "info": 0,
                "purpose": "DYNAMIC",
                "size": 64,
                "symbol": "",
                "type": "RELATIVE",
            },
            {
                "address": 16344,
                "info": 1,
                "purpose": "DYNAMIC",
                "size": 64,
                "symbol": "__libc_start_main",
                "type": "GLOB_DAT",
            },
            {
                "address": 16352,
                "info": 2,
                "purpose": "DYNAMIC",
                "size": 64,
                "symbol": "_ITM_deregisterTMCloneTable",
                "type": "GLOB_DAT",
            },
            {
                "address": 16360,
                "info": 4,
                "purpose": "DYNAMIC",
                "size": 64,
                "symbol": "__gmon_start__",
                "type": "GLOB_DAT",
            },
            {
                "address": 16368,
                "info": 5,
                "purpose": "DYNAMIC",
                "size": 64,
                "symbol": "_ITM_registerTMCloneTable",
                "type": "GLOB_DAT",
            },
            {
                "address": 16376,
                "info": 6,
                "purpose": "DYNAMIC",
                "size": 64,
                "symbol": "__cxa_finalize",
                "type": "GLOB_DAT",
            },
            {
                "address": 16336,
                "info": 3,
                "purpose": "PLTGOT",
                "size": 64,
                "symbol": "puts",
                "type": "JUMP_SLOT",
            },
        ],
        "sections": [
            {
                "alignment": 0,
                "entropy": 0.0,
                "flags": [],
                "name": "",
                "offset": 0,
                "size": 0,
                "type": "NULL",
                "segments": [],
            },
            {
                "alignment": 1,
                "entropy": 3.940759832540089,
                "flags": ["ALLOC"],
                "name": ".interp",
                "offset": 792,
                "size": 28,
                "type": "PROGBITS",
                "segments": ["INTERP", "LOAD"],
            },
            {
                "alignment": 8,
                "entropy": 1.9345480540338138,
                "flags": ["ALLOC"],
                "name": ".note.gnu.property",
                "offset": 824,
                "size": 48,
                "type": "NOTE",
                "segments": ["LOAD", "NOTE", "GNU_PROPERTY"],
            },
            {
                "alignment": 4,
                "entropy": 4.080500530640266,
                "flags": ["ALLOC"],
                "name": ".note.gnu.build-id",
                "offset": 872,
                "size": 36,
                "type": "NOTE",
                "segments": ["LOAD", "NOTE"],
            },
            {
                "alignment": 4,
                "entropy": 1.561278124459133,
                "flags": ["ALLOC"],
                "name": ".note.ABI-tag",
                "offset": 908,
                "size": 32,
                "type": "NOTE",
                "segments": ["LOAD", "NOTE"],
            },
            {
                "alignment": 8,
                "entropy": 1.6430827743914267,
                "flags": ["ALLOC"],
                "name": ".gnu.hash",
                "offset": 944,
                "size": 36,
                "type": "GNU_HASH",
                "segments": ["LOAD"],
            },
            {
                "alignment": 8,
                "entropy": 0.5870934129890327,
                "flags": ["ALLOC"],
                "name": ".dynsym",
                "offset": 984,
                "size": 168,
                "type": "DYNSYM",
                "segments": ["LOAD"],
            },
            {
                "alignment": 1,
                "entropy": 4.642271790628106,
                "flags": ["ALLOC"],
                "name": ".dynstr",
                "offset": 1152,
                "size": 141,
                "type": "STRTAB",
                "segments": ["LOAD"],
            },
            {
                "alignment": 2,
                "entropy": 1.610577243331642,
                "flags": ["ALLOC"],
                "name": ".gnu.version",
                "offset": 1294,
                "size": 14,
                "type": "HIOS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 8,
                "entropy": 2.3020440502629658,
                "flags": ["ALLOC"],
                "name": ".gnu.version_r",
                "offset": 1312,
                "size": 48,
                "type": "GNU_VERNEED",
                "segments": ["LOAD"],
            },
            {
                "alignment": 8,
                "entropy": 1.3272473878703939,
                "flags": ["ALLOC"],
                "name": ".rela.dyn",
                "offset": 1360,
                "size": 192,
                "type": "RELA",
                "segments": ["LOAD"],
            },
            {
                "alignment": 8,
                "entropy": 0.9833557549816874,
                "flags": ["INFO_LINK", "ALLOC"],
                "name": ".rela.plt",
                "offset": 1552,
                "size": 24,
                "type": "RELA",
                "segments": ["LOAD"],
            },
            {
                "alignment": 4,
                "entropy": 4.236368983644952,
                "flags": ["ALLOC", "EXECINSTR"],
                "name": ".init",
                "offset": 4096,
                "size": 27,
                "type": "PROGBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 16,
                "entropy": 3.558157328518199,
                "flags": ["ALLOC", "EXECINSTR"],
                "name": ".plt",
                "offset": 4128,
                "size": 32,
                "type": "PROGBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 16,
                "entropy": 3.375,
                "flags": ["ALLOC", "EXECINSTR"],
                "name": ".plt.got",
                "offset": 4160,
                "size": 16,
                "type": "PROGBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 16,
                "entropy": 3.375,
                "flags": ["ALLOC", "EXECINSTR"],
                "name": ".plt.sec",
                "offset": 4176,
                "size": 16,
                "type": "PROGBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 16,
                "entropy": 5.114732343297649,
                "flags": ["ALLOC", "EXECINSTR"],
                "name": ".text",
                "offset": 4192,
                "size": 263,
                "type": "PROGBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 4,
                "entropy": 3.2389012566026305,
                "flags": ["ALLOC", "EXECINSTR"],
                "name": ".fini",
                "offset": 4456,
                "size": 13,
                "type": "PROGBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 4,
                "entropy": 3.41041725276052,
                "flags": ["ALLOC"],
                "name": ".rodata",
                "offset": 8192,
                "size": 17,
                "type": "PROGBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 4,
                "entropy": 3.095479202232869,
                "flags": ["ALLOC"],
                "name": ".eh_frame_hdr",
                "offset": 8212,
                "size": 52,
                "type": "PROGBITS",
                "segments": ["LOAD", "GNU_EH_FRAME"],
            },
            {
                "alignment": 8,
                "entropy": 3.477075817903484,
                "flags": ["ALLOC"],
                "name": ".eh_frame",
                "offset": 8264,
                "size": 172,
                "type": "PROGBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 8,
                "entropy": 1.061278124459133,
                "flags": ["WRITE", "ALLOC"],
                "name": ".init_array",
                "offset": 11704,
                "size": 8,
                "type": "INIT_ARRAY",
                "segments": ["LOAD", "GNU_RELRO"],
            },
            {
                "alignment": 8,
                "entropy": 0.5435644431995964,
                "flags": ["WRITE", "ALLOC"],
                "name": ".fini_array",
                "offset": 11712,
                "size": 8,
                "type": "FINI_ARRAY",
                "segments": ["LOAD", "GNU_RELRO"],
            },
            {
                "alignment": 8,
                "entropy": 1.4564336815986219,
                "flags": ["WRITE", "ALLOC"],
                "name": ".dynamic",
                "offset": 11720,
                "size": 496,
                "type": "DYNAMIC",
                "segments": ["LOAD", "DYNAMIC", "GNU_RELRO"],
            },
            {
                "alignment": 8,
                "entropy": 0.4206545402614363,
                "flags": ["WRITE", "ALLOC"],
                "name": ".got",
                "offset": 12216,
                "size": 72,
                "type": "PROGBITS",
                "segments": ["LOAD", "GNU_RELRO"],
            },
            {
                "alignment": 8,
                "entropy": 0.6685644431995964,
                "flags": ["WRITE", "ALLOC"],
                "name": ".data",
                "offset": 12288,
                "size": 16,
                "type": "PROGBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 1,
                "entropy": 2.75,
                "flags": ["WRITE", "ALLOC"],
                "name": ".bss",
                "offset": 12304,
                "size": 8,
                "type": "NOBITS",
                "segments": ["LOAD"],
            },
            {
                "alignment": 1,
                "entropy": 3.935955649986687,
                "flags": ["MERGE", "STRINGS"],
                "name": ".comment",
                "offset": 12304,
                "size": 37,
                "type": "PROGBITS",
                "segments": [],
            },
            {
                "alignment": 8,
                "entropy": 1.7068900631460535,
                "flags": [],
                "name": ".symtab",
                "offset": 12344,
                "size": 864,
                "type": "SYMTAB",
                "segments": [],
            },
            {
                "alignment": 1,
                "entropy": 4.8437883286856245,
                "flags": [],
                "name": ".strtab",
                "offset": 13208,
                "size": 481,
                "type": "STRTAB",
                "segments": [],
            },
            {
                "alignment": 1,
                "entropy": 4.270277599965863,
                "flags": [],
                "name": ".shstrtab",
                "offset": 13689,
                "size": 282,
                "type": "STRTAB",
                "segments": [],
            },
        ],
        "segments": [
            {
                "alignment": 8,
                "file_offset": 64,
                "physical": {"address": 64, "size": 728},
                "sections": [],
                "type": "PHDR",
                "virtual": {"address": 64, "size": 728},
            },
            {
                "alignment": 1,
                "file_offset": 792,
                "physical": {"address": 792, "size": 28},
                "sections": ["interp"],
                "type": "INTERP",
                "virtual": {"address": 792, "size": 28},
            },
            {
                "alignment": 4096,
                "file_offset": 0,
                "physical": {"address": 0, "size": 1576},
                "sections": [
                    "interp",
                    "note",
                    "note",
                    "note",
                    "gnu",
                    "dynsym",
                    "dynstr",
                    "gnu",
                    "gnu",
                    "rela",
                    "rela",
                ],
                "type": "LOAD",
                "virtual": {"address": 0, "size": 1576},
            },
            {
                "alignment": 4096,
                "file_offset": 4096,
                "physical": {"address": 4096, "size": 373},
                "sections": ["init", "plt", "plt", "plt", "text", "fini"],
                "type": "LOAD",
                "virtual": {"address": 4096, "size": 373},
            },
            {
                "alignment": 4096,
                "file_offset": 8192,
                "physical": {"address": 8192, "size": 244},
                "sections": ["rodata", "eh_frame_hdr", "eh_frame"],
                "type": "LOAD",
                "virtual": {"address": 8192, "size": 244},
            },
            {
                "alignment": 4096,
                "file_offset": 11704,
                "physical": {"address": 15800, "size": 600},
                "sections": [
                    "init_array",
                    "fini_array",
                    "dynamic",
                    "got",
                    "data",
                    "bss",
                ],
                "type": "LOAD",
                "virtual": {"address": 15800, "size": 608},
            },
            {
                "alignment": 8,
                "file_offset": 11720,
                "physical": {"address": 15816, "size": 496},
                "sections": ["dynamic"],
                "type": "DYNAMIC",
                "virtual": {"address": 15816, "size": 496},
            },
            {
                "alignment": 8,
                "file_offset": 824,
                "physical": {"address": 824, "size": 48},
                "sections": ["note"],
                "type": "NOTE",
                "virtual": {"address": 824, "size": 48},
            },
            {
                "alignment": 4,
                "file_offset": 872,
                "physical": {"address": 872, "size": 68},
                "sections": ["note", "note"],
                "type": "NOTE",
                "virtual": {"address": 872, "size": 68},
            },
            {
                "alignment": 8,
                "file_offset": 824,
                "physical": {"address": 824, "size": 48},
                "sections": ["note"],
                "type": "GNU_PROPERTY",
                "virtual": {"address": 824, "size": 48},
            },
            {
                "alignment": 4,
                "file_offset": 8212,
                "physical": {"address": 8212, "size": 52},
                "sections": ["eh_frame_hdr"],
                "type": "GNU_EH_FRAME",
                "virtual": {"address": 8212, "size": 52},
            },
            {
                "alignment": 16,
                "file_offset": 0,
                "physical": {"address": 0, "size": 0},
                "sections": [],
                "type": "GNU_STACK",
                "virtual": {"address": 0, "size": 0},
            },
            {
                "alignment": 1,
                "file_offset": 11704,
                "physical": {"address": 15800, "size": 584},
                "sections": ["init_array", "fini_array", "dynamic", "got"],
                "type": "GNU_RELRO",
                "virtual": {"address": 15800, "size": 584},
            },
        ],
        "symbols": {
            "exported": [
                "_fini",
                "__dso_handle",
                "_IO_stdin_used",
                "_start",
                "main",
                "__TMC_END__",
                "_init",
            ],
            "imported": [
                "__libc_start_main",
                "puts",
                "__cxa_finalize",
                "__libc_start_main@GLIBC_2.34",
                "puts@GLIBC_2.2.5",
                "__cxa_finalize@GLIBC_2.2.5",
            ],
            "libraries": ["libc.so.6"],
            "table": [
                {
                    "binding": "LOCAL",
                    "information": 0,
                    "function": False,
                    "symbol": "",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "* Local *",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 18,
                    "function": True,
                    "symbol": "__libc_start_main",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": True,
                    "version": "GLIBC_2.34(2)",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "WEAK",
                    "information": 32,
                    "function": False,
                    "symbol": "_ITM_deregisterTMCloneTable",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "* Global *",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 18,
                    "function": True,
                    "symbol": "puts",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": True,
                    "version": "GLIBC_2.2.5(3)",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "WEAK",
                    "information": 32,
                    "function": False,
                    "symbol": "__gmon_start__",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "* Global *",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "WEAK",
                    "information": 32,
                    "function": False,
                    "symbol": "_ITM_registerTMCloneTable",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "* Global *",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "WEAK",
                    "information": 34,
                    "function": True,
                    "symbol": "__cxa_finalize",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "GLIBC_2.2.5(3)",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 0,
                    "function": False,
                    "symbol": "",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 4,
                    "function": False,
                    "symbol": "Scrt1.o",
                    "section_index": "ABS",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FILE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 1,
                    "function": False,
                    "symbol": "__abi_tag",
                    "section_index": "???",
                    "size": 32,
                    "static": False,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 4,
                    "function": False,
                    "symbol": "crtstuff.c",
                    "section_index": "ABS",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FILE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 2,
                    "function": True,
                    "symbol": "deregister_tm_clones",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 2,
                    "function": True,
                    "symbol": "register_tm_clones",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 2,
                    "function": True,
                    "symbol": "__do_global_dtors_aux",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 1,
                    "function": False,
                    "symbol": "completed.0",
                    "section_index": "???",
                    "size": 1,
                    "static": False,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 1,
                    "function": False,
                    "symbol": "__do_global_dtors_aux_fini_array_entry",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 2,
                    "function": True,
                    "symbol": "frame_dummy",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 1,
                    "function": False,
                    "symbol": "__frame_dummy_init_array_entry",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 4,
                    "function": False,
                    "symbol": "hello_world.c",
                    "section_index": "ABS",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FILE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 4,
                    "function": False,
                    "symbol": "crtstuff.c",
                    "section_index": "ABS",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FILE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 1,
                    "function": False,
                    "symbol": "__FRAME_END__",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 4,
                    "function": False,
                    "symbol": "",
                    "section_index": "ABS",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FILE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 1,
                    "function": False,
                    "symbol": "_DYNAMIC",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 0,
                    "function": False,
                    "symbol": "__GNU_EH_FRAME_HDR",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "LOCAL",
                    "information": 1,
                    "function": False,
                    "symbol": "_GLOBAL_OFFSET_TABLE_",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 18,
                    "function": True,
                    "symbol": "__libc_start_main@GLIBC_2.34",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "WEAK",
                    "information": 32,
                    "function": False,
                    "symbol": "_ITM_deregisterTMCloneTable",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "WEAK",
                    "information": 32,
                    "function": False,
                    "symbol": "data_start",
                    "section_index": "???",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 18,
                    "function": True,
                    "symbol": "puts@GLIBC_2.2.5",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 16,
                    "function": False,
                    "symbol": "_edata",
                    "section_index": "???",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 18,
                    "function": True,
                    "symbol": "_fini",
                    "section_index": "???",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "HIDDEN",
                },
                {
                    "binding": "GLOBAL",
                    "information": 16,
                    "function": False,
                    "symbol": "__data_start",
                    "section_index": "???",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "WEAK",
                    "information": 32,
                    "function": False,
                    "symbol": "__gmon_start__",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 17,
                    "function": False,
                    "symbol": "__dso_handle",
                    "section_index": "???",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "HIDDEN",
                },
                {
                    "binding": "GLOBAL",
                    "information": 17,
                    "function": False,
                    "symbol": "_IO_stdin_used",
                    "section_index": "???",
                    "size": 4,
                    "static": True,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 16,
                    "function": False,
                    "symbol": "_end",
                    "section_index": "???",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 18,
                    "function": True,
                    "symbol": "_start",
                    "section_index": "???",
                    "size": 38,
                    "static": True,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 16,
                    "function": False,
                    "symbol": "__bss_start",
                    "section_index": "???",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 18,
                    "function": True,
                    "symbol": "main",
                    "section_index": "???",
                    "size": 30,
                    "static": True,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 17,
                    "function": False,
                    "symbol": "__TMC_END__",
                    "section_index": "???",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "OBJECT",
                    "variable": True,
                    "visibility": "HIDDEN",
                },
                {
                    "binding": "WEAK",
                    "information": 32,
                    "function": False,
                    "symbol": "_ITM_registerTMCloneTable",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "NOTYPE",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "WEAK",
                    "information": 34,
                    "function": True,
                    "symbol": "__cxa_finalize@GLIBC_2.2.5",
                    "section_index": "UNDEF",
                    "size": 0,
                    "static": False,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "DEFAULT",
                },
                {
                    "binding": "GLOBAL",
                    "information": 18,
                    "function": True,
                    "symbol": "_init",
                    "section_index": "???",
                    "size": 0,
                    "static": True,
                    "version": "None",
                    "type": "FUNC",
                    "variable": False,
                    "visibility": "HIDDEN",
                },
            ],
        },
    }

    scanner_event = run_test_scan(
        mocker=mocker,
        scan_class=ScanUnderTest,
        fixture_path=Path(__file__).parent / "fixtures/test.elf",
    )

    TestCase.maxDiff = None
    TestCase().assertDictEqual(test_scan_event, scanner_event)