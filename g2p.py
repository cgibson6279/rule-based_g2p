"""Portuguese g2p rules."""

import pynini

from pynini.lib import rewrite


# Gets all characters in language English
chars = (
    [chr(i) for i in range(65, 90)]
    + [chr(i) for i in range(97, 123)]
    + ["ʎ", "ʃ", "ɲ", "ç", "á", "ʁ", "ɾ", "ʒ", "ch", "lh", "nh", "ss"]
)
SIGMA_STAR = pynini.string_map(chars).closure()
# Portugese rule set given
G2P = (
    pynini.cdrewrite(
        pynini.union(
            pynini.cross("ch", "ʃ"),
            pynini.cross("lh", "ʎ"),
            pynini.cross("nh", "ɲ"),
        ),
        "",
        "",
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(pynini.cross("h", ""), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(
        pynini.cross("o", "u"), "", pynini.union("[EOS]", "s", "r"), SIGMA_STAR
    )
    @ pynini.cdrewrite(
        pynini.cross("e", "i"),
        "",
        pynini.union("[EOS]", pynini.accep("s[EOS]")),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("c", "s"), "", pynini.union("i", "e"), SIGMA_STAR
    )
    @ pynini.cdrewrite(pynini.cross("c", "k"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(
        pynini.cross("s", "z"),
        pynini.union("a", "e", "i", "o", "u"),
        pynini.union("a", "e", "i", "o", "u"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(pynini.cross("z", "s"), "", "[EOS]", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ç", "s"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("ss", "s"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("rr", "ʁ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("r", "ʁ"), "[BOS]", "", SIGMA_STAR)
    @ pynini.cdrewrite(
        pynini.cross(
            "r",
            "ɾ",
        ),
        pynini.union("a", "e"),
        "",
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross(
            "r",
            "ɾ",
        ),
        "",
        pynini.union("a", "e", "i"),
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(pynini.cross("á", "a"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("t", "tʃ"), "", "i", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("d", "dʒ"), "", "i", SIGMA_STAR)
)


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
