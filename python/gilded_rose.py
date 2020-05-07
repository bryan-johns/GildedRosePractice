# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if "Sulfuras" in item.name: # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
                continue

            multiplier = 1 # I'm using a multiplier to track if something is conjured. Who knows, maybe you'll have a conjured Aged Brie someday
            if "Conjured" in item.name:
                multiplier = 2

            if "Aged Brie" in item.name:
                if item.sell_in == 0:
                    item.quality += 2 * multiplier
                else:
                    item.quality += 1 * multiplier

            elif "Backstage passes" in item.name:
                if item.sell_in == 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality += 3 * multiplier
                elif item.sell_in <= 10:
                    item.quality += 2 * multiplier
                else:
                    item.quality += 1 * multiplier

            else:
                if item.quality == 0:
                    continue
                if item.sell_in == 0:
                    item.quality -= 2 * multiplier
                else:
                    item.quality -= 1 * multiplier

            if item.quality >= 50:
                item.quality = 50

            if item.sell_in != 0:
                item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
