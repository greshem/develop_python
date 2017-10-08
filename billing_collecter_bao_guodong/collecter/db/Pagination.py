# -*- coding:utf-8 -*-
'''
Created on 2014-7-4

@author: baoguodong.kevin
'''
class PageResult(list):
    
    def __init__(self, total=0, page_no=1, page_size=15, edge_size=0):
        """
        total:总记录数
        page_no:当前页数
        page_size：每页记录条数
        edge_size:滑窗的大小
        """
        self.total = total
        self.page_size = page_size if page_size > 0 else 0
        self.edge_size = edge_size if edge_size > 0 else 0

        if page_no <= 0:
            self.no = 1
        elif self.max >= 1 and page_no > self.max:
            self.no = self.max
        else:
            self.no = page_no

    @property
    def start(self):
        return (self.no - 1) * self.page_size

    @property
    def max(self):
        """总页数"""
        if self.page_size > 0:
            return (self.total + self.page_size - 1) / self.page_size
        else:  # 不分页，显示全部条目
            return 1

    @property
    def has_prev(self):
        """是否有上一页"""
        return self.no > 1

    @property
    def has_next(self):
        """是否有下一页"""
        return self.no < self.max

    @property
    def slider(self):
        """显示滑窗大小"""
        if self.edge_size > 0:
            start = max(self.no - self.edge_size, 1)
            stop = min(self.no + self.edge_size, self.max)
        else: 
            start, stop = 1, self.max
        return range(start, stop + 1)

    def clear(self):
        del self[:]

    def page_dict(self):
        page = {"curr_page":self.no, "data_count":self.total, "page_count":self.max}
        page["has_prev"], page["has_next"] = self.has_prev, self.has_next
        page["page_range"] = self.slider
        return page


class Pagination(object):

    def __init__(self, query):
        self.query = query

    def all(self, offset=0, limit=0):
        if limit == 0:
            return self.query.all()
        else:
            return self.query.offset(offset).limit(limit).all()  # SQLAlchemy orm
            return self.query.all()[offset : offset + limit]  # Django orm

    def count(self):
        return self.query.count()

    def head(self):
        return self.query.first()

    def paginate(self, page_no=1, page_size=15, edge_size=0):
        result = PageResult(self.count(), page_no, page_size, edge_size)
        result.extend(self.all(result.start, result.page_size))
        return result
