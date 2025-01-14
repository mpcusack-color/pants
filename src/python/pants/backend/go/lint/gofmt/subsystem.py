# Copyright 2021 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.option.subsystem import Subsystem
from pants.util.docutil import bin_name


class GofmtSubsystem(Subsystem):
    options_scope = "gofmt"
    help = "Gofmt-specific options."

    @classmethod
    def register_options(cls, register):
        super().register_options(register)
        register(
            "--skip",
            type=bool,
            default=False,
            help=f"Don't use gofmt when running `{bin_name()} fmt` and `{bin_name()} lint`.",
        )
