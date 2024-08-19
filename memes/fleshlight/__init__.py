from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import FrameAlignPolicy, Maker, make_gif_or_combined_gif
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def fleshlight(images: list[BuildImage], texts, args):
    params = [
        (((0, 6), (205, 0), (213, 157), (8, 171)), (117, 59)),
        (((0, 6), (205, 0), (213, 157), (8, 171)), (117, 59)),
        (((0, 6), (205, 0), (213, 157), (8, 171)), (117, 59)),
        (((0, 7), (204, 0), (213, 157), (8, 172)), (118, 58)),
        (((0, 6), (207, 0), (213, 158), (8, 173)), (119, 57)),
        (((0, 6), (207, 0), (213, 158), (8, 173)), (119, 57)),
        (((0, 6), (207, 0), (213, 158), (8, 173)), (119, 57)),
        (((0, 6), (205, 0), (212, 157), (7, 171)), (121, 58)),
        (((0, 6), (205, 0), (212, 157), (7, 171)), (121, 58)),
        (((0, 6), (206, 0), (212, 158), (8, 172)), (121, 56)),
        (((0, 6), (206, 0), (212, 158), (8, 172)), (121, 56)),
        (((0, 6), (207, 0), (214, 157), (10, 171)), (121, 55)),
        (((0, 7), (201, 0), (218, 154), (13, 169)), (121, 49)),
        (((0, 7), (195, 0), (219, 147), (18, 162)), (118, 50)),
        (((0, 4), (196, 0), (223, 133), (18, 143)), (114, 54)),
        (((0, 0), (192, 1), (219, 121), (17, 124)), (115, 58)),
        (((0, 0), (188, 5), (220, 110), (20, 107)), (112, 61)),
        (((0, 0), (185, 15), (217, 86), (26, 73)), (108, 72)),
        (((0, 0), (182, 19), (234, 67), (34, 44)), (102, 88)),
        (((0, 0), (175, 25), (224, 55), (22, 23)), (111, 105)),
        (((0, 0), (167, 29), (209, 49), (13, 14)), (121, 110)),
        (((0, 0), (144, 27), (195, 46), (8, 8)), (135, 110)),
        (((0, 0), (177, 36), (206, 59), (13, 18)), (129, 93)),
        (((0, 0), (180, 38), (211, 69), (16, 25)), (126, 83)),
        (((0, 0), (181, 28), (220, 70), (26, 39)), (119, 82)),
        (((0, 0), (180, 17), (227, 65), (27, 45)), (115, 89)),
        (((0, 0), (181, 15), (230, 63), (33, 46)), (110, 95)),
        (((0, 0), (184, 24), (228, 73), (27, 47)), (91, 102)),
        (((0, 0), (189, 8), (208, 73), (0, 66)), (83, 94)),
        (((19, 0), (202, 25), (204, 85), (0, 58)), (63, 82)),
        (((12, 0), (196, 18), (205, 70), (0, 50)), (70, 87)),
        (((4, 0), (189, 17), (205, 74), (0, 53)), (82, 79)),
        (((0, 0), (184, 18), (205, 72), (1, 51)), (91, 74)),
        (((0, 0), (183, 17), (206, 69), (4, 52)), (92, 73)),
    ]

    def maker(i: int) -> Maker:
        def make(imgs: list[BuildImage]) -> BuildImage:
            img = imgs[0].convert("RGBA").resize((210, 170), keep_ratio=True)
            frame = BuildImage.open(img_dir / f"{i}.png")
            points, pos = params[i]
            frame.paste(img.perspective(points), pos, below=True)
            return frame

        return make

    return make_gif_or_combined_gif(
        images, maker, 34, 0.1, FrameAlignPolicy.extend_first
    )


add_meme(
    "fleshlight",
    fleshlight,
    min_images=1,
    max_images=1,
    keywords=["飞机杯"],
    date_created=datetime(2023, 4, 29),
    date_modified=datetime(2023, 4, 29),
)
