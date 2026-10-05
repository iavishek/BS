import pyhtml as h

t = h.html(
        h.head(
            h.title('Test page')
        ),
        h.body(
            h.h1('This is a article'),
            h.div('This is some text'),
            h.div(h.h2('inside title'),
                h.p('some text in a paragraph.'))
        )
    )


print(t.render())