# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_quality_control(self):
        items = [
                 Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
                 Item(name="Aged Brie", sell_in=2, quality=0),
                 Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
                 Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
                ]

        days = 5
        gilded_rose = GildedRose(items)

        for day in range(days):
            gilded_rose.update_quality()

        self.assertEquals(15, items[0].quality)
        self.assertEquals(8, items[1].quality)
        self.assertEquals(2, items[2].quality)
        self.assertEquals(80, items[3].quality)
        self.assertEquals(80, items[4].quality)
        self.assertEquals(25, items[5].quality)
        self.assertEquals(59, items[6].quality)
        self.assertEquals(64, items[7].quality)
        self.assertEquals(0, items[8].quality)

    def test_sell_in_control(self):
        items = [
                 Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
                 Item(name="Aged Brie", sell_in=2, quality=0),
                 Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
                 Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
                ]

        days = 5
        gilded_rose = GildedRose(items)

        for day in range(days):
            gilded_rose.update_quality()

        self.assertEquals(5, items[0].sell_in)
        self.assertEquals(0, items[1].sell_in)
        self.assertEquals(0, items[2].sell_in)
        self.assertEquals(0, items[3].sell_in)
        self.assertEquals(-1, items[4].sell_in)
        self.assertEquals(10, items[5].sell_in)
        self.assertEquals(5, items[6].sell_in)
        self.assertEquals(0, items[7].sell_in)
        self.assertEquals(0, items[8].sell_in)

if __name__ == '__main__':
    unittest.main()
