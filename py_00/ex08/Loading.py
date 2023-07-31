def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start = 1
    fill = '█'
    with_size = 60
    for item in lst:
        yield item
        progress = start / total
        filled_length = int(with_size * progress)
        bar = fill * filled_length + (' ' * (with_size - filled_length))
        print(f'\r{progress:.0%}|{bar}| {start}/{total}', end='', flush=True)
        start += 1
    print()
