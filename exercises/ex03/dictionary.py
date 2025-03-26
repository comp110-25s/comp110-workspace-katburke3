"""a place to store function skeletons"""

__author__: str = "730558066"


def invert(forwards: dict[str, str]) -> dict[str, str]:
    backwards: dict[str, str] = {}
    for key in forwards:
        new_key: str = forwards[key]
        new_values: str = key
        if new_key in backwards:
            raise KeyError("duplicate keys are trying to be added")
        backwards[new_key] = new_values
    return backwards


def count(words: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}
    idx: int = 0
    while idx < len(words):
        if words[idx] in count_dict:
            count_dict[words[idx]] += 1
        else:
            count_dict[words[idx]] = 1
        idx += 1
    return count_dict


def favorite_color(favs: dict[str, str]) -> str:
    fav_col_count: dict[str, int] = {}
    colors: list[str] = []
    for key in favs:
        colors.append(favs[key])
    fav_col_count = count(colors)
    fav: int = 0
    for value in fav_col_count:
        if fav_col_count[value] > fav:
            fav = fav_col_count[value]
    return str(fav)


def bin_len(word_list: list[str]) -> dict[int, set[str]]:
    group_lengths: dict[int, set[str]] = {}
    for word in word_list:
        if len(word) in group_lengths:
            group_lengths[len(word)].add(word)
        else:
            group_lengths[len(word)] = set()
            group_lengths[len(word)].add(word)
    return group_lengths
