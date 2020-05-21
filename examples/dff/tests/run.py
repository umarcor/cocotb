from pathlib import Path
from vunit import VUnit

ROOT = Path(__file__).resolve().parent.parent

vu = VUnit.from_argv()

vu.add_library("lib").add_source_files([
    ROOT / 'hdl' / '*.vhdl',
    ROOT / 'tests' / '*.vhdl'
])

vu.main()
