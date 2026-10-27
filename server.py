@app.get("/")
def read_root():
    try:
        doc = Document(r"C:\Users\user\Documents\Лабораторная 2.docx")

        # Собираем весь текст в одну строку
        full_text = "\n".join([p.text for p in doc.paragraphs])

        # Разбиваем на строки и форматируем
        lines = full_text.split("\n")
        formatted_lines = []

        for line in lines:
            if line.strip():  # Если строка не пустая
                # Добавляем отступ в 4 пробела (как красную строку)
                formatted_lines.append("    " + line.strip())
            else:
                # Если пустая, оставляем как есть (для разделения абзацев)
                formatted_lines.append("")

        # Собираем обратно
        result_text = "\n".join(formatted_lines)

        return {"text": result_text}

    except Exception as e:
        return {"error": str(e)}