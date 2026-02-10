def build_notes_from_chunks(chunks: list[str], total_duration: int):
    notes = []
    max_sections = max(1, total_duration//8)
    selected_chunks = chunks[:max_sections]
    per_section_time = total_duration // len(selected_chunks)
    for idx, chunk in enumerate(selected_chunks, start=1):
        notes.append({
        "heading":f"Section {idx}",
        "explanation":chunk[:800]
    })
    return notes
