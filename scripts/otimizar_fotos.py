#!/usr/bin/env python3
"""
Otimiza as fotos da galeria de obras (opcional, roda no seu computador).

- Lê JPG, JPEG, PNG e WebP da pasta assets/obras/ (ou da pasta informada).
- Corrige a rotação da foto de celular (EXIF).
- Redimensiona para no máximo 1600 px de largura (nunca amplia).
- Salva em WebP na mesma pasta, com o mesmo nome e extensão .webp.
- Mostra a largura e a altura finais, que você copia para o index.html.

Requisitos:  Python 3.8+ e Pillow  →  pip install Pillow

Uso (a partir da pasta do site):
    python scripts/otimizar_fotos.py
    python scripts/otimizar_fotos.py --qualidade 80 --largura 1600
    python scripts/otimizar_fotos.py --apagar-originais
    python scripts/otimizar_fotos.py caminho/da/pasta
"""
import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow não encontrado. Instale com:  pip install Pillow")

EXTENSOES = {".jpg", ".jpeg", ".png", ".webp"}
PASTA_PADRAO = Path(__file__).resolve().parent.parent / "assets" / "obras"


def otimizar(arquivo: Path, largura_max: int, qualidade: int) -> tuple:
    destino = arquivo.with_suffix(".webp")
    with Image.open(arquivo) as img:
        img = ImageOps.exif_transpose(img)
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGBA" if "A" in img.getbands() else "RGB")
        if img.width > largura_max:
            nova_altura = round(img.height * largura_max / img.width)
            img = img.resize((largura_max, nova_altura), Image.LANCZOS)
        img.save(destino, "WEBP", quality=qualidade, method=6)
        return destino, img.width, img.height


def main() -> None:
    parser = argparse.ArgumentParser(description="Converte fotos da galeria para WebP otimizado.")
    parser.add_argument("pasta", nargs="?", default=str(PASTA_PADRAO), help="pasta com as fotos (padrão: assets/obras)")
    parser.add_argument("--largura", type=int, default=1600, help="largura máxima em pixels (padrão: 1600)")
    parser.add_argument("--qualidade", type=int, default=80, help="qualidade WebP de 1 a 100 (padrão: 80)")
    parser.add_argument("--apagar-originais", action="store_true", help="apaga o JPG/PNG original após converter")
    args = parser.parse_args()

    pasta = Path(args.pasta)
    if not pasta.is_dir():
        sys.exit(f"Pasta não encontrada: {pasta}")

    fotos = sorted(p for p in pasta.iterdir() if p.suffix.lower() in EXTENSOES)
    if not fotos:
        print(f"Nenhuma foto encontrada em {pasta}")
        return

    print(f"Otimizando {len(fotos)} foto(s) em {pasta}\n")
    for foto in fotos:
        tamanho_antes = foto.stat().st_size
        try:
            destino, largura, altura = otimizar(foto, args.largura, args.qualidade)
        except Exception as erro:  # foto corrompida ou formato não suportado
            print(f"  ERRO  {foto.name}: {erro}")
            continue
        tamanho_depois = destino.stat().st_size
        print(
            f"  {foto.name} → {destino.name}  "
            f'width="{largura}" height="{altura}"  '
            f"{tamanho_antes / 1024:.0f} KB → {tamanho_depois / 1024:.0f} KB"
        )
        if args.apagar_originais and foto.suffix.lower() != ".webp":
            foto.unlink()

    print("\nPronto. Copie width/height de cada foto para o <img> correspondente no index.html.")


if __name__ == "__main__":
    main()
