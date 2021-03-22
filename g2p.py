"""Portuguese g2p rules."""

import pynini

from pynini.lib import rewrite


# TODO: define SIGMA_STAR as an FST representing the closure over the union of
# graphemes and phonemes. Don't forget to remove this comment when you're done.
SIGMA_STAR = ...

# TODO: define G2P as an FST implementing the g2p rules.
# Don't forget to remove this comment when you're done.
G2P = ...


def g2p(istring: str) -> str:
    """Applies the G2P rule.

    Args:
      istring: the graphemic input string.

    Returns:
      The phonemic output string.

    Raises.
      rewrite.Error: composition failure.
    """
    return rewrite.one_top_rewrite(istring, G2P)
