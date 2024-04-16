## Этот файл предназначен для тестирования sets_program.py
import unittest

from sets_program import HashTable
from sets_program import PowerSet

class MyTests(unittest.TestCase):

    def test1(self): # возможность добавления отсутствующего элемента и невозможность добавления присутствующего в множестве элемента с помощью put()
        x = PowerSet(19, 3)
        x.put('13')
        self.assertEqual(x.get('13'), True)

    def test2(self): # возможность добавления отсутствующего элемента и невозможность добавления присутствующего в множестве элемента с помощью put()
        x = PowerSet(19, 3)
        x.put('13')
        x.put('13')
        self.assertEqual(x.remove('13'), True)
        self.assertEqual(x.remove('13'), False)

    def test3(self): # возможность добавления отсутствующего элемента и невозможность добавления присутствующего в множестве элемента с помощью put()
        x = PowerSet(19, 3)
        x.put('13')
        x.put('14')
        x.put('15')
        x.put('15')
        self.assertEqual(x.remove('13'), True)
        self.assertEqual(x.remove('14'), True)
        self.assertEqual(x.remove('15'), True)
        self.assertEqual(x.remove('15'), False)

    def test4(self): # удаление элемента с помощью remove()
        x = PowerSet(19, 3)
        x.put('13')
        x.put('14')
        x.put('15')
        self.assertEqual(x.remove('13'), True)
        self.assertEqual(x.get('13'), False)

    def test5(self): # удаление элемента с помощью remove()
        x = PowerSet(19, 3)
        x.put('13')
        x.put('14')
        x.put('15')
        self.assertEqual(x.remove('15'), True)
        self.assertEqual(x.get('15'), False)

        self.assertEqual(x.remove('14'), True)
        self.assertEqual(x.get('14'), False)

        self.assertEqual(x.remove('13'), True)
        self.assertEqual(x.get('13'), False)

    def test6(self): # пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(19, 3)
        x.put('13')
        x.put('14')
        x.put('15')
        y = PowerSet(19, 3)
        y.put('14')
        y.put('15')
        y.put('16')
        mn = x.intersection(y)
        self.assertEqual(mn.get('13'), False)
        self.assertEqual(mn.get('14'), True)
        self.assertEqual(mn.get('15'), True)
        self.assertEqual(mn.get('16'), False)

    def test7(self): # пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(19, 3)
        x.put('100')
        x.put('210')
        x.put('220')
        y = PowerSet(19, 3)
        y.put('310')
        y.put('320')
        y.put('100') 
        mn = x.intersection(y)
        self.assertEqual(mn.get('100'), True)
        self.assertEqual(mn.get('210'), False)
        self.assertEqual(mn.get('220'), False)
        self.assertEqual(mn.get('310'), False)
        self.assertEqual(mn.get('320'), False)

    def test8(self): # пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(10, 2)
        x.put('15')
        x.put('14')
        x.put('13')
        y = PowerSet(5, 2)
        y.put('13')
        y.put('14')
        y.put('15')
        mn = x.intersection(y)
        self.assertEqual(mn.get('13'), True)
        self.assertEqual(mn.get('14'), True)
        self.assertEqual(mn.get('15'), True)

    def test9(self): # пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(10, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        y.put('21')
        y.put('22')
        y.put('23')
        self.assertEqual(x.intersection(y), None)

    def test10(self): # пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(10, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        self.assertEqual(x.intersection(y), None)

    def test11(self): # пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(10, 2)
        y = PowerSet(5, 2)
        y.put('21')
        y.put('22')
        y.put('23')
        self.assertEqual(x.intersection(y), None)


    def test12(self): # объединение union(), когда оба параметра непустые, и когда один из параметров -- пустое множество
        x = PowerSet(10, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        y.put('21')
        y.put('22')
        y.put('23')
        mn = x.union(y)
        self.assertEqual(mn.get('11'), True)
        self.assertEqual(mn.get('12'), True)
        self.assertEqual(mn.get('13'), True)
        self.assertEqual(mn.get('21'), True)
        self.assertEqual(mn.get('22'), True)
        self.assertEqual(mn.get('23'), True)

    def test13(self): # объединение union(), когда оба параметра непустые, и когда один из параметров -- пустое множество
        x = PowerSet(10, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        mn = x.union(y)
        self.assertEqual(mn.get('11'), True)
        self.assertEqual(mn.get('12'), True)
        self.assertEqual(mn.get('13'), True)

    def test14(self): # объединение union(), когда оба параметра непустые, и когда один из параметров -- пустое множество
        x = PowerSet(5, 2)
        y = PowerSet(5, 2)
        y.put('11')
        y.put('12')
        y.put('13')
        mn = x.union(y)
        self.assertEqual(mn.get('11'), True)
        self.assertEqual(mn.get('12'), True)
        self.assertEqual(mn.get('13'), True)

    def test15(self): # разница difference(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(5, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        y.put('11')
        mn = x.difference(y)
        self.assertEqual(mn.get('11'), False)
        self.assertEqual(mn.get('12'), True)
        self.assertEqual(mn.get('13'), True)

    def test16(self): # разница difference(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(5, 2)
        x.put('10')
        x.put('20')
        x.put('30')
        y = PowerSet(5, 2)
        y.put('10')
        y.put('20')
        mn = x.difference(y)
        self.assertEqual(mn.get('10'), False)
        self.assertEqual(mn.get('20'), False)
        self.assertEqual(mn.get('30'), True)

    def test17(self): # разница difference(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(5, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        y.put('11')
        mn = x.difference(y)
        self.assertEqual(mn.get('11'), False)
        self.assertEqual(mn.get('12'), True)
        self.assertEqual(mn.get('13'), True)

    def test18(self): # разница difference(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(5, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        y.put('11')
        y.put('12')
        y.put('13')
        self.assertEqual(x.difference(y), None)

    def test19(self): # разница difference(), чтобы в результате получались как пустое, так и непустое множества
        x = PowerSet(5, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        mn = x.difference(y)
        self.assertEqual(mn.get('11'), True)
        self.assertEqual(mn.get('12'), True)
        self.assertEqual(mn.get('13'), True)

    def test20(self): # подмножество issubset()
        x = PowerSet(5, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        y.put('11')
        y.put('12')
        y.put('13')
        self.assertEqual(x.issubset(y), True)

    def test21(self): # подмножество issubset()
        x = PowerSet(5, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        y = PowerSet(5, 2)
        y.put('11')
        y.put('12')
        y.put('13')
        y.put('14')
        self.assertEqual(x.issubset(y), False)

    def test22(self): # подмножество issubset()
        x = PowerSet(5, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        x.put('14')
        y = PowerSet(5, 2)
        y.put('11')
        y.put('12')
        y.put('13')
        self.assertEqual(x.issubset(y), True)

    def test23(self): # подмножество issubset()
        x = PowerSet(5, 2)
        x.put('11')
        x.put('12')
        x.put('13')
        x.put('14')
        y = PowerSet(5, 2)
        y.put('11')
        self.assertEqual(x.issubset(y), True)

    def test24(self): # подмножество issubset()
        x = PowerSet(100, 5)
        x.put('11')
        y = PowerSet(5, 2)
        y.put('11')
        self.assertEqual(x.issubset(y), True)

    def test25(self):
        x = PowerSet(100, 5)
        x.put('11')
        with self.assertRaises(ValueError):
            y = PowerSet(0, 2)

    def test26(self):
        x = PowerSet(100, 5)
        x.put('11')
        with self.assertRaises(ValueError):
            y = PowerSet(5, 0)

if __name__ == '__main__':
    unittest.main()