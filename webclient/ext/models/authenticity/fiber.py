from typing import List

from webclient import gen


class FiberChecks(gen.AuthenticityCheckResult):

    @gen.AuthenticityCheckResult.list.getter
    def list(self) -> List[gen.FiberResult]:
        # noinspection PyTypeChecker
        return super().list
