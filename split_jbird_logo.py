from collections import deque
from pathlib import Path
from PIL import Image


def build_mask(img, white_threshold=245):
    w, h = img.size
    px = img.load()
    mask = [[False] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a > 10 and not (r > white_threshold and g > white_threshold and b > white_threshold):
                mask[y][x] = True
    return mask


def connected_components(mask):
    h = len(mask)
    w = len(mask[0]) if h else 0
    visited = [[False] * w for _ in range(h)]
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    components = []

    for y in range(h):
        for x in range(w):
            if mask[y][x] and not visited[y][x]:
                q = deque([(x, y)])
                visited[y][x] = True
                minx = maxx = x
                miny = maxy = y
                count = 0

                while q:
                    cx, cy = q.popleft()
                    count += 1
                    minx = min(minx, cx)
                    miny = min(miny, cy)
                    maxx = max(maxx, cx)
                    maxy = max(maxy, cy)

                    for dx, dy in neighbors:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < w and 0 <= ny < h and mask[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((nx, ny))

                components.append((count, minx, miny, maxx, maxy))

    return components


def make_white_transparent(img, white_threshold=245):
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if r > white_threshold and g > white_threshold and b > white_threshold:
                px[x, y] = (255, 255, 255, 0)


def split_logo(input_path: Path, output_dir: Path):
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size

    mask = build_mask(img)
    components = connected_components(mask)
    components = [c for c in components if c[0] > 100]
    components.sort(key=lambda c: c[0], reverse=True)

    if len(components) < 2:
        raise RuntimeError(f"Could not detect two separate birds. Found {len(components)} major components.")

    birds = components[:2]
    birds.sort(key=lambda c: c[1])  # left to right

    created = []
    for i, (_, minx, miny, maxx, maxy) in enumerate(birds, start=1):
        pad = 10
        x0 = max(0, minx - pad)
        y0 = max(0, miny - pad)
        x1 = min(w, maxx + pad + 1)
        y1 = min(h, maxy + pad + 1)

        crop = img.crop((x0, y0, x1, y1)).convert("RGBA")
        make_white_transparent(crop)

        out_path = output_dir / f"Jbird Logo - Bird {i}.png"
        crop.save(out_path)
        created.append(out_path)

    return created


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    source = root / "Jbird Logo.png"
    outputs = split_logo(source, root)
    print("Created:")
    for out in outputs:
        print(out.name)
