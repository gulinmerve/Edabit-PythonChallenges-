###https://edabit.com/challenge/yPzfgnDsPWXwH7dMq

class Pagination(object):
    index = 0
    def __init__(self, alph, divide):
        super(Pagination, self).__init__()
        self.alph = alph
        self.divide = divide
    def getVisibleItems(self):
        def split(word):
            return [char for char in word]
        print(split(self.alph[Pagination.index:self.divide]))
    def nextPage(self):
        Pagination.index += 4
        self.divide += 4
        return self # p.nextPage().nextPage() yapmasi icin
    def fisrtPage(self):
        Pagination.index = 0
        self.divide = 4
        return self
    def lastPage(self):
        totalpage = int(len(self.alph)/4)
        Pagination.index = totalpage * 4
        self.divide = len(self.alph)
        return self
    def goToPage(self, pageNumber):
        if pageNumber > int(len(self.alph) / 4) + 1:
            print("Out of index ...")
        else:
            Pagination.index = (pageNumber - 1) * 4
            self.divide = ((pageNumber - 1) * 4) + 4
        return self
alphabetList = "abcdefghijklmnopqrstuvwxyz"
p = Pagination(alphabetList, 4)
print(p.getVisibleItems())
print(p.nextPage())

###
class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = (len(items)//pageSize) + \
                           (1 if len(items) % pageSize else 0)
        self.currentPage = 1
    def getItems(self):
        return self.items
    def getPageSize(self):
        return self.pageSize
    def getCurrentPage(self):
        return self.currentPage
    def prevPage(self):
        if self.currentPage != 1:
            self.currentPage -= 1
        return self
    def nextPage(self):
        if self.currentPage != self.totalPages:
            self.currentPage += 1
        return self
    def firstPage(self):
        self.currentPage = 1
        return self
    def lastPage(self):
        self.currentPage = self.totalPages
        return self
    def goToPage(self, pageNum):
        if 1 < int(pageNum) <= self.totalPages:
            self.currentPage = int(pageNum)
        elif int(pageNum) <= 1:
            self.currentPage = 1
        else:
            self.currentPage = self.totalPages
        return self
    def getVisibleItems(self):
        return self.items[(self.currentPage-1)*self.pageSize:self.currentPage*self.pageSize]
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.getVisibleItems())  # ["a", "b", "c", "d"]
p.nextPage()
print(p.getVisibleItems())  # ['e', 'f', 'g', 'h']
p.lastPage()
print(p.getVisibleItems())  # ["y", "z"]