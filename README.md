# Site institucional — Gestecno Engenharia

Site de uma página da **GESTECNO ENGENHARIA LTDA**, feito em HTML + CSS + JavaScript puro,
sem framework e sem etapa de build. Pronto para publicar na Vercel em
`https://gestecnoengenharia.com.br`.

> **Status:** layout final, galeria com lightbox e dados da empresa prontos.
> Falta preencher os itens `[A CONFIRMAR]` (principalmente WhatsApp, Instagram e fotos reais).

---

## Estrutura

```
gestecno-engenharia-site-/
├── index.html                  # página única com todas as seções
├── css/style.css               # estilos (cores e fontes em :root)
├── js/main.js                  # menu, lightbox da galeria, animações de entrada, ano do rodapé
├── assets/
│   ├── img/                    # logo, favicon, imagem do hero, imagem de compartilhamento (og)
│   ├── obras/                  # fotos da galeria (WebP)
│   └── portfolio/
│       └── portfolio-gestecno.pdf   # PLACEHOLDER — substituir pelo portfólio real
├── scripts/otimizar_fotos.py   # opcional: converte fotos para WebP (máx. 1600 px)
├── favicon.ico
├── robots.txt
├── sitemap.xml
├── vercel.json                 # cabeçalhos de cache e segurança (inclui Content-Security-Policy)
└── .vercelignore               # README e scripts não são publicados
```

---

## Rodar localmente

Não há instalação. Basta servir a pasta com qualquer servidor estático
(abrir o `index.html` direto no navegador também funciona, mas alguns caminhos
absolutos como `/css/style.css` só resolvem via servidor).

```bash
cd gestecno-engenharia-site-

# opção 1 — Python (já vem no macOS/Linux)
python3 -m http.server 8080

# opção 2 — Node
npx serve .
```

Acesse `http://localhost:8080`.

---

## Placeholders a preencher

Todo conteúdo pendente aparece **destacado em amarelo** na página e segue o formato
`[A CONFIRMAR: descrição]`. Para encontrar todos, busque no editor por:

```
[A CONFIRMAR
```

Além disso, há **2 marcadores dentro de links** (não aparecem como texto). Troque todos
com "Localizar e substituir":

| Marcador            | O que colocar                                                       | Exemplo            |
|---------------------|---------------------------------------------------------------------|--------------------|
| `55DDDNUMERO`       | WhatsApp/telefone: 55 + DDD + número, **só dígitos**                 | `5594999998888`    |
| `USUARIO_INSTAGRAM` | usuário do Instagram, sem `@`                                       | `gestecnoeng`      |

> Se o telefone fixo for diferente do WhatsApp, troque o `tel:+55DDDNUMERO`
> manualmente (seção Contato).

### Dados já preenchidos (fonte: cartão CNPJ da Receita Federal)

Endereço da sede (Parauapebas/PA) e e-mail
`comercial@gestecnoengenharia.com.br`. Razão social e CNPJ aparecem só no rodapé e nos
dados estruturados (SEO), que não são visíveis na página.
Os **cards de Serviços** e os **Diferenciais** foram escritos a partir das atividades
registradas no CNPJ (CNAEs) — revise com a empresa e ajuste ao que ela realmente executa hoje.
O telefone do cartão CNPJ, `(94) 9215-5221`, tem só 8 dígitos e pode estar desatualizado; por isso
o telefone e o WhatsApp continuam como `[A CONFIRMAR]`.

### Lista do que falta, por seção

**`<head>` / SEO (index.html)**
- [ ] JSON-LD: `telephone` e `areaServed` (cidades/região atendida)
- [ ] JSON-LD `sameAs`: usuário do Instagram

**Apresentação (hero)**
- [ ] Foto do hero: substituir `assets/img/hero.webp` por uma foto real de obra, horizontal, ~1920×1080
      (a imagem atual é uma ilustração provisória; o site já aplica uma camada azul por cima para o texto ficar legível)

**Quem somos**
- [ ] História e perfil (quem fundou, tipos de obra, público atendido, região de atuação)
- [ ] Quadro lateral: responsável técnico (nome + CREA/CAU)

**Serviços, Como trabalhamos e Diferenciais**
- [ ] Revisar os textos baseados nos CNAEs
- [ ] Confirmar se as 4 etapas de "Como trabalhamos" refletem o processo real da empresa

**Obras**
- [ ] 6 fotos reais em `assets/obras/` + `alt` de cada uma
- [ ] Legenda de cada obra: nome, cidade/UF, serviço executado (na `figcaption` **e** no `data-caption`)

**Contato**
- [ ] Número do WhatsApp (exibido e no link) e telefone
- [ ] @ do Instagram
- [ ] Portfólio: substituir `assets/portfolio/portfolio-gestecno.pdf` (manter o mesmo nome)

**Arquivos**
- [ ] `sitemap.xml`: atualizar `<lastmod>` quando publicar

---

## Trocar cores e fontes

Tudo está em variáveis no início de `css/style.css`:

```css
:root {
  --color-primary: #00188f;   /* azul da logo */
  --color-accent:  #fe7501;   /* laranja da logo */
  --color-steel:   #48657f;   /* cinza-azulado da engrenagem */
  --font-heading: "Exo 2", ...;
  --font-body:    "Inter", ...;
}
```

Ao trocar a fonte, ajuste também o link do Google Fonts no `<head>` do `index.html`.

---

## Adicionar fotos na galeria

1. Coloque as fotos (JPG/PNG) em `assets/obras/`, com nomes simples, sem espaços nem acentos
   (ex.: `obra-07.jpg`).
2. *(Opcional, recomendado)* Converta para WebP com no máximo 1600 px de largura:
   ```bash
   pip install Pillow
   python scripts/otimizar_fotos.py --apagar-originais
   ```
   O script mostra `width` e `height` de cada foto.
3. No `index.html`, seção `id="obras"`, copie um bloco `<li class="gallery__item">…</li>`
   inteiro e ajuste:
   - `href` e `src` → caminho da foto (`/assets/obras/obra-07.webp`)
   - `width` e `height` → valores mostrados pelo script
   - `alt` → descrição do que aparece na foto
   - `data-caption` → texto da legenda ampliada
   - `<figcaption>` → nome da obra, cidade/UF e serviço
4. Mantenha `loading="lazy"` em todas as fotos da galeria.

---

## Publicar na Vercel

> ⚠️ Nada é publicado automaticamente. Siga estes passos quando o conteúdo estiver aprovado.

Este repositório contém só o site, então a raiz do projeto é a própria raiz do repositório.

1. Acesse <https://vercel.com/new> e importe o repositório `gestecno-engenharia-site-` do GitHub.
2. **Framework Preset:** `Other`. Deixe *Root Directory* como `./`, *Build Command* e
   *Install Command* vazios e *Output Directory* como `.` (padrão).
3. Clique em **Deploy**. A Vercel gera um endereço provisório (`*.vercel.app`) — confira o site nele.

### Conectar o domínio gestecnoengenharia.com.br

1. No projeto da Vercel: **Settings → Domains → Add**.
2. Adicione `gestecnoengenharia.com.br` **e** `www.gestecnoengenharia.com.br`.
   Escolha qual será o principal (recomendado: sem `www`) e deixe o outro redirecionando.
3. A Vercel mostrará os registros DNS a criar. Normalmente são:

| Tipo  | Nome (no Registro.br) | Valor                     |
|-------|-----------------------|---------------------------|
| A     | *(vazio / raiz)*      | `76.76.21.21`             |
| CNAME | `www`                 | `cname.vercel-dns.com.`   |

> Use sempre os valores **exibidos no painel da Vercel** — eles podem mudar.

### Configurar no Registro.br

1. Entre em <https://registro.br> → **Meus domínios** → `gestecnoengenharia.com.br`.
2. Em **DNS**, confira se está usando os servidores do Registro.br
   (*"Utilizar os servidores DNS do Registro.br"*). Se o DNS estiver em outro provedor
   (ex.: provedor de e-mail ou hospedagem antiga), faça as alterações **lá**.
3. Clique em **Configurar zona DNS / Editar zona**.
4. **Antes de alterar qualquer coisa, tire um print ou anote todos os registros existentes.**
5. Adicione/edite **apenas**:
   - o registro **A** da raiz → `76.76.21.21`
     (se já existir um A da raiz apontando para outra hospedagem, substitua só ele);
   - o registro **CNAME** `www` → `cname.vercel-dns.com.`
     (se existir um A para `www`, remova esse A, pois não pode haver A e CNAME no mesmo nome).
6. Salve. A propagação costuma levar de minutos a algumas horas.
7. Volte em **Settings → Domains** na Vercel e aguarde o status *Valid Configuration*.
   O certificado HTTPS é emitido automaticamente.

> 🚫 **NÃO apague registros MX, TXT (SPF, DKIM, DMARC, verificação do Google/Microsoft)
> nem CNAMEs de e-mail (`autodiscover`, `mail`, etc.).** Eles mantêm o e-mail da empresa
> funcionando. Mexa somente no A da raiz e no `www`.

### Depois de publicar

- Teste o site no celular e no computador.
- Teste os links de WhatsApp, telefone, e-mail, Instagram e o download do portfólio.
- Valide os dados estruturados em <https://search.google.com/test/rich-results>.
- (Opcional) Cadastre o site no Google Search Console e envie o `sitemap.xml`.

---

## Segurança (Content-Security-Policy)

O `vercel.json` só permite carregar scripts, estilos e imagens do próprio site, e fontes do
Google Fonts. Se no futuro você incluir algo externo (mapa incorporado, vídeo do YouTube,
pixel de anúncio, analytics), será preciso liberar o domínio correspondente no cabeçalho
`Content-Security-Policy`; caso contrário, o recurso será bloqueado pelo navegador.

## Decisões técnicas

- **Sem cookies e sem analytics.**
- Imagens com `width`/`height` declarados (evita "pulos" de layout), `loading="lazy"` em tudo
  exceto o hero, formato WebP.
- Acessibilidade: link "Pular para o conteúdo", foco visível, menu acessível por teclado
  (Esc fecha), `alt` em todas as imagens, textos de link indicam quando abrem nova aba,
  contraste verificado (botão laranja usa texto azul-escuro).
- Sem JavaScript, o menu fica aberto e as fotos da galeria abrem como link direto.
