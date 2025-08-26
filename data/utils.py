import random
import datetime


def get_user() -> str:
    first_names = [
        "James",
        "John",
        "Robert",
        "Michael",
        "William",
        "David",
        "Richard",
        "Joseph",
        "Thomas",
        "Charles",
        "Christopher",
        "Daniel",
        "Matthew",
        "Anthony",
        "Mark",
        "Donald",
        "Steven",
        "Paul",
        "Andrew",
        "Joshua",
        "Mary",
        "Patricia",
        "Jennifer",
        "Linda",
        "Elizabeth",
    ]

    last_names = [
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Miller",
        "Davis",
        "Rodriguez",
        "Martinez",
        "Hernandez",
        "Lopez",
        "Gonzalez",
        "Wilson",
        "Anderson",
        "Thomas",
        "Taylor",
        "Moore",
        "Jackson",
        "Martin",
    ]

    return f"{random.choice(first_names)} {random.choice(last_names)}"


def get_time(
    start: datetime = datetime.datetime.now(), end: datetime = datetime.datetime.now()
) -> datetime:
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + datetime.timedelta(seconds=random_seconds)


def get_id(start: int = 1000, end: int = 9999) -> int:
    return random.randint(start, end)


def get_ip() -> str:
    return ".".join(str(random.randint(1, 255)) for _ in range(4))


def get_page() -> str:
    pages = [
        "/home",
        "/search",
        "/product",
        "/cart",
        "/checkout",
        "/profile",
        "/orders",
        "/wishlist",
        "/faq",
        "/contact",
    ]
    return random.choice(pages)


def get_device() -> str:
    devices = ["mobile", "desktop", "tablet", "smart_tv", "wearable"]
    return random.choice(devices)
