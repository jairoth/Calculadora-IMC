import flet as ft

def main(page: ft.Page):
    page.title = "BMI/IMC Global Pro"
    page.theme_mode = "dark"
    page.window_width = 380
    page.window_height = 780 
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"

    textos = {
        "pt": {
            "titulo": "Calculadora IMC", "peso": "Peso (kg)", "altura": "Altura (cm)", "cintura": "Cintura (cm)",
            "botao": "CALCULAR", "limpar": "LIMPAR", "anuncio": "ESPAÇO PUBLICITÁRIO", "btn_completo": "CÁLCULO IMC COMPLETO",
            "meta_perder": "Meta: Queimar {} kcal/dia para perder {} kg em 90 dias.",
            "meta_ganhar": "Meta: Ingerir {} kcal extras/dia para ganhar {} kg em 90 dias.",
            "parabens": "Normal - Parabéns, agora é só manter!",
            "rce_bom": "Cintura-Altura: {:.2f} (Saudável)", "rce_ruim": "Cintura-Altura: {:.2f} (Risco Cardiovascular)",
            "dica_perder": "Dica: Troque o pão/refrigerante por água e corra {} min/dia.",
            "dica_ganhar": "Dica: Adicione gorduras boas (azeite, abacate) e proteínas.",
            "erro": "Valores inválidos!"
        },
        "en": {
            "titulo": "BMI Calculator", "peso": "Weight (kg)", "altura": "Height (cm)", "cintura": "Waist (cm)",
            "botao": "CALCULATE", "limpar": "CLEAR", "anuncio": "ADVERTISING SPACE", "btn_completo": "COMPLETE BMI CALC",
            "meta_perder": "Goal: Burn {} kcal/day to lose {} kg in 90 days.",
            "meta_ganhar": "Goal: Add {} extra kcal/day to gain {} kg in 90 days.",
            "parabens": "Normal - Congratulations, just maintain it!",
            "rce_bom": "Waist-Height: {:.2f} (Healthy)", "rce_ruim": "Waist-Height: {:.2f} (Cardio Risk)",
            "dica_perder": "Tip: Swap bread/soda for water and run {} min/day.",
            "dica_ganhar": "Tip: Add healthy fats (oil, avocado) and proteins.",
            "erro": "Invalid values!"
        },
        "es": {
            "titulo": "Calculadora IMC", "peso": "Peso (kg)", "altura": "Altura (cm)", "cintura": "Cintura (cm)",
            "botao": "CALCULAR", "limpar": "LIMPIAR", "anuncio": "ESPACIO PUBLICITARIO", "btn_completo": "CÁLCULO COMPLETO",
            "meta_perder": "Meta: Quemar {} kcal/día para perder {} kg en 90 días.",
            "meta_ganhar": "Meta: Ingerir {} kcal extras/día para ganar {} kg en 90 días.",
            "parabens": "Normal - ¡Felicidades, mantenlo así!",
            "rce_bom": "Cintura-Altura: {:.2f} (Saludable)", "rce_ruim": "Cintura-Altura: {:.2f} (Riesgo Cardio)",
            "dica_perder": "Tip: Cambie pan/refresco por agua y corra {} min/día.",
            "dica_ganhar": "Tip: Agregue grasas saludables y proteínas.",
            "erro": "¡Valores inválidos!"
        },
        "zh": {
            "titulo": "BMI 计算器", "peso": "体重 (kg)", "altura": "身高 (cm)", "cintura": "腰围 (cm)",
            "botao": "计算", "limpar": "清除", "anuncio": "广告位", "btn_completo": "完整 IMC 计算",
            "meta_perder": "目标：每天燃烧 {} kcal，90天内减重 {} kg。",
            "meta_ganhar": "目标：每天增加 {} kcal，90天内增重 {} kg。",
            "parabens": "正常 - 恭喜，请保持！",
            "rce_bom": "腰高比: {:.2f} (健康)", "rce_ruim": "腰高比: {:.2f} (心血管风险)",
            "dica_perder": "建议：少吃面包/汽水，每天跑步 {} 分钟。",
            "dica_ganhar": "建议：增加优质脂肪（鳄梨、橄榄油）和蛋白质。",
            "erro": "数值无效！"
        }
    }

    idioma = "pt"

    def calcular(e):
        try:
            p = float(entry_peso.value.replace(",", "."))
            a_val = float(entry_altura.value.replace(",", "."))
            a = a_val / 100 if a_val > 3 else a_val
            
            imc = p / (a * a)
            peso_meta = p * 0.10
            kcal_dia = (peso_meta * 7700) / 90
            minutos_corrida = int(kcal_dia / 10) 

            if imc < 16: res, cor = "Magreza Grau III", "red900"
            elif imc < 17: res, cor = "Magreza Grau II", "orange700"
            elif imc < 18.5: res, cor = "Magreza Grau I", "blue200"
            elif imc < 25: res, cor = textos[idioma]["parabens"], "green400"
            elif imc < 30: res, cor = "Sobrepeso", "yellow400"
            elif imc < 35: res, cor = "Obesidade I", "orange400"
            elif imc < 40: res, cor = "Obesidade II", "red400"
            else: res, cor = "Obesidade III (Mórbida)", "red900"

            label_resultado.value = f"IMC: {imc:.2f}\n{res}"
            label_resultado.color = cor

            if imc < 18.5:
                label_meta.value = textos[idioma]["meta_ganhar"].format(f"{kcal_dia:,.0f}", f"{peso_meta:.1f}")
                label_dica.value = textos[idioma]["dica_ganhar"]
            elif imc < 25:
                label_meta.value = ""
                label_dica.value = ""
            else:
                label_meta.value = textos[idioma]["meta_perder"].format(f"{kcal_dia:,.0f}", f"{peso_meta:.1f}")
                label_dica.value = textos[idioma]["dica_perder"].format(minutos_corrida)

            if entry_cintura.visible and entry_cintura.value:
                c_val = float(entry_cintura.value.replace(",", "."))
                rce = c_val / (a * 100)
                if rce <= 0.5:
                    label_rce.value = textos[idioma]["rce_bom"].format(rce)
                    label_rce.color = "green200"
                else:
                    label_rce.value = textos[idioma]["rce_ruim"].format(rce)
                    label_rce.color = "red200"
            page.update()
        except:
            label_resultado.value = textos[idioma]["erro"]
            label_resultado.color = "red"
            page.update()

    def mudar_idioma(novo_idioma):
        nonlocal idioma
        idioma = novo_idioma
        label_titulo.value = textos[idioma]["titulo"]
        entry_peso.label = textos[idioma]["peso"]
        entry_altura.label = textos[idioma]["altura"]
        entry_cintura.label = textos[idioma]["cintura"]
        btn_calc.text = textos[idioma]["botao"]
        btn_limpar.text = textos[idioma]["limpar"]
        btn_completo.text = textos[idioma]["btn_completo"]
        label_ads.content.value = textos[idioma]["anuncio"]
        page.update()

    def criar_btn_idioma(emoji, lang):
        return ft.Container(
            content=ft.Text(emoji, size=25),
            on_click=lambda _: mudar_idioma(lang),
            border=ft.border.all(1, "white"),
            border_radius=8, padding=5
        )

    estilo_label = ft.TextStyle(color="white")
    entry_peso = ft.TextField(label=textos[idioma]["peso"], text_align="center", width=220, border_color="white", label_style=estilo_label)
    entry_altura = ft.TextField(label=textos[idioma]["altura"], text_align="center", width=220, border_color="white", label_style=estilo_label)
    entry_cintura = ft.TextField(label=textos[idioma]["cintura"], text_align="center", width=220, visible=False, border_color="white", label_style=estilo_label)
    label_ads = ft.Container(content=ft.Text(textos[idioma]["anuncio"], text_align="center", weight="bold"), margin=10, padding=20, bgcolor="bluegrey900", border_radius=10, alignment=ft.Alignment(0,0))
    label_titulo = ft.Text(textos[idioma]["titulo"], size=32, weight="bold")
    btn_calc = ft.ElevatedButton(textos[idioma]["botao"], on_click=calcular, width=220, bgcolor="blue700", color="white")
    
    def abrir_cintura(e):
        entry_cintura.visible = True
        btn_completo.visible = False
        page.update()

    btn_completo = ft.TextButton(textos[idioma]["btn_completo"], on_click=abrir_cintura, style=ft.ButtonStyle(color="blue200"))
    
    def reset(e):
        entry_peso.value = entry_altura.value = entry_cintura.value = ""
        entry_cintura.visible = False
        btn_completo.visible = True
        label_resultado.value = label_rce.value = label_meta.value = label_dica.value = ""
        page.update()

    btn_limpar = ft.TextButton(textos[idioma]["limpar"], on_click=reset, style=ft.ButtonStyle(color="white"))
    label_resultado = ft.Text("", size=20, weight="bold", text_align="center")
    label_rce = ft.Text("", size=16, weight="bold", text_align="center")
    label_meta = ft.Text("", size=14, color="grey400", text_align="center")
    label_dica = ft.Text("", size=14, color="yellow400", weight="bold", text_align="center")

    idiomas_row = ft.Row([criar_btn_idioma("🇧🇷", "pt"), criar_btn_idioma("🇺🇸", "en"), criar_btn_idioma("🇪🇸", "es"), criar_btn_idioma("🇨🇳", "zh")], alignment="center")

    page.add(label_ads, idiomas_row, ft.Container(height=5), label_titulo, entry_peso, entry_altura, entry_cintura, ft.Container(height=10), btn_calc, btn_completo, btn_limpar, label_resultado, label_rce, label_meta, label_dica)

if __name__ == "__main__":
    ft.app(target=main)