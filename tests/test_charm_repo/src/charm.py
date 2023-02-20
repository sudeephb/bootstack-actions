#!/usr/bin/env python3
# Copyright 2023 Robert Gildein
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk


from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus


class TestCharmCharm(CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        """Test Charm."""
        super().__init__(*args)
        self.unit.status = ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    main(TestCharmCharm)
