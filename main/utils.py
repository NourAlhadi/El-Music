def stars(reviews):
    all_reviews = 0
    star = 0

    for review in reviews.iterator():
        star += review.stars
        all_reviews += 1

    star /= max(all_reviews, 1)
    star = round(star)
    return -star


def rates(reviews):
    reviews = reviews.all()
    return -len(reviews)


def name(name):
    return name
