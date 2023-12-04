def ft_tqdm(lst: range) -> None:

    for item in lst:
        progress_percent = (item / len(lst)) * 100
        print(f"{progress_percent:.0f}%|[{'=' * int(progress_percent / 2):<50}]| {item}/{len(lst)}", end='\r')
        yield item

