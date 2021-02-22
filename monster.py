from dataclasses import dataclass


@dataclass
class Monster:
    climate: str
    frequency: str
    organization: str
    activity_cycle: str
    diet: str
    intelligence: str
    treasure: str
    alignment: str
    num_appearing: int
    armor_class: int
    movement: str
    hit_dice: str
    thac0: int
    num_attacks: int
    damage_per_attack: str
    special_attacks: str
    special_defenses: str
    magic_resistance: str
    size: str
    morale: str
    xp_value: int

    @classmethod
    def from_table(cls, table):
        return cls(
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(1) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(2) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(3) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(4) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(5) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(6) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(7) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(8) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(9) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(10) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(11) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(12) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(13) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(14) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(15) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(16) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(17) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(18) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(19) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(20) > td:nth-child(2)"
            ).text,
            table.find_element_by_css_selector(
                "body > table > tbody > tr:nth-child(21) > td:nth-child(2)"
            ).text,
        )