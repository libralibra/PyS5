#! /usr/bin/env python
import datetime

def ProcessHTML(content):
    return content.replace('\n','<br>')

class Slide(object):
    ''' the slide class represents one slide '''

    def __init__(self,title,content='',handout=''):
        self.title_ = title
        self.content_ = content.replace('\n','<br>')
        self.handout_ = handout.replace('\n','<br>')
        self.layer_ = 1

    def setTitle(self,title):
        self.title_ = title

    def setContent(self,content):
        self.content_ = content

    def addContent(self,content):
        self.content_ += "<br>"+content.replace('\n','<br>')

    def setHandout(self,handout):
        self.handout_ = handout.replace('\n','<br>')

    def addHandout(self,handout):
        self.handout_ += '<br>'+handout.replace('\n','<br>')

    def __repr__(self):
        retStr = '<div class="slide">\n'
        retStr += '<h1>'+self.title_+'</h1>\n'
        retStr += '<div class="slidecontent">\n'+self.content_.replace('\n','<br>')+'\n</div>\n'
        retStr += '<div class="handout">'+self.handout_.replace('\n','<br>')+'</div>\n'
        retStr += '</div>\n'
        return retStr

class Preface(Slide):
    ''' preface of the PPT '''

    def __init__(self,title,align='left'):
        #super(Preface,self).__init__(title)
        Slide(title)
        self.setAlign(align)

    def setAlign(self,align='left'):
        self.align_ = align

    def __repr__(self):
        retStr = '<div class="slide">\n'
        retStr += '<div class="slidecontent">\n'+self.content_+'\n</div>\n'
        retStr += '</div>\n'
        return retStr

class Head(object):
    ''' Head information of PPT '''

    def __init__(self, title, author, args={}):
        self.author_ = author
        self.title_ = title
        if len(args)==0:
            self.metadata_ = {'name="version"' : 'S5 1.1',
                        'name="generator"' : 'PyS5',
                        'name="presentdate"' : str(datetime.date.today()),
                        'name="author"' : self.author_,
                        'name="company"' : '',
                        'name="defaultView"' : 'slideshow',
                        'name="controlVis"' : 'visible',
                        'http-equiv="Content-Type"' : ''
                        }
        else:
            self.metadata_ = args

    def setView(self,view):
        ''' set the view type: slideshow or outline '''
        self.metadata_['name="defaultView"'] = view

    def setControl(self,flag=True):
        ''' set if show control '''
        self.metadata_['name="controlVis"'] = flag and 'visible' or 'hidden'

    def setVersion(self,version):
        self.metadata_['version'] = version

    def __repr__(self):
        self.retStr = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>''' + self.title_ + '</title>\n'
        for k,v in self.metadata_.items():
            self.retStr += ('<meta ' + k + ' content="' + v + '" />\n')
        self.retStr += '''<!-- style sheet links -->
<link rel="stylesheet" href="ui/default/slides.css" type="text/css" media="projection" id="slideProj" />
<link rel="stylesheet" href="ui/default/outline.css" type="text/css" media="screen" id="outlineStyle" />
<link rel="stylesheet" href="ui/default/print.css" type="text/css" media="print" id="slidePrint" />
<link rel="stylesheet" href="ui/default/opera.css" type="text/css" media="projection" id="operaFix" />
<!-- S5 JS -->
<script src="ui/default/slides.js" type="text/javascript"></script>\n</head>\n'''
        return self.retStr

class Layout(object):
    ''' layout class '''

    def __init__(self, args={}):
        if len(args)!=0:
            self.header_ = args['header']
            self.footer_ = args['footer']
            self.topleft_ = args['topleft']
            self.topright_ = args['topright']
            self.bottomleft_ = args['bottomleft']
            self.bottomright_ = args['bottomright']
        else:
            self.header_ = ''
            self.footer_ = ''
            self.topleft_ = ''
            self.topright_ = ''
            self.bottomleft_ = ''
            self.bottomright_ = ''

    def setHeader(self,header):
        self.header_ = header

    def setFooter(self,footer):
        self.footer_ = footer

    def setTopLeft(self,topleft):
        self.topleft_ = topleft

    def setTopRight(self,topright):
        self.topright_ = topright

    def setBottomLeft(self,bottomleft):
        self.bottomleft_ = bottomleft

    def setBottomRight(self,bottomright):
        self.bottomright_ = bottomright

    def __repr__(self):
        retStr = '''<body>\n<!-- layout -->
<div class="layout">
<div id="controls"><!-- DO NOT EDIT --></div>
<div id="currentSlide"><!-- DO NOT EDIT --></div>\n'''
        retStr += '<div id="header">'+self.header_+'</div>\n'
        retStr += '<div id="footer">'+self.footer_+'</div>\n'
        retStr += '<div class="topleft">'+self.topleft_+"</div>\n"
        retStr += '<div class="topright">'+self.topright_+"</div>\n"
        retStr += '<div class="bottomleft">'+self.bottomleft_+"</div>\n"
        retStr += '<div class="bottomright">'+self.bottomright_+"</div>\n</div>\n\n"
        return retStr

class PPT(object):
    ''' the PPT class represents the whole presentation '''

    def __init__(self,title,subtitle,author,datenow=str(datetime.date.today()),slides=[]):
        ''' initialise the PPT class with title, author and optional parameter
            date and slides list
        '''
        self.slides_ = []
        self.num_ = len(slides)
        self.title_ = title
        self.subtitle_ = subtitle
        self.author_ = author
        self.date_ = datenow
        self.version_ = 'S5 1.1'
        self.header_ = Head(self.title_,self.author_)
        self.layout_ = Layout()
        self.preface_ = Preface(self.title_,'right')
        self.preface_.setContent('<div align="'+self.preface_.align_+'">\n<h1>'+self.title_+'</h1>\n<h2>'+self.subtitle_+'</h2>\n<h3>'+self.author_+'</h3>\n<h5>'+self.date_+'</h5>\n</div>')
        self.slides_.append(self.preface_)
        self.slides_.extend(slides)

    def setTitle(self,title):
        ''' set the title of PPT, the title of the whole presentation '''
        self.title_ = title

    def setDate(self,datenow):
        self.date_ = datenow

    def setAuthor(self,author):
        self.author_ = author

    def setSlides(self,slides):
        self.slides_ = slides
        self.num_ = len(self.slides_)

    def addSlides(self,slide):
        self.slides_.append(slide)

    def __repr__(self):
        retStr = str(self.header_)
        retStr += str(self.layout_)
        retStr += '<!-- presentation slides -->\n<div class="presentation">\n\n'
        for slide in self.slides_:
            retStr += str(slide)+'\n'
        retStr += '</div>\n</body>\n</html>'
        return retStr

# test function
def unitTest():
    slide = Slide('test slide','<ol><li>test1</li><li>test2</li></ol>')
    ppt = PPT('[test ppt]','[subtitle]','daniel',str(datetime.date.today()),[slide])
    ppt.setTitle("")
    fout = open(r's5-blank\test.html','w')
    fout.write(str(ppt))
    fout.close()
    print 'DONE'

# unit test
if __name__=='__main__':
    unitTest()