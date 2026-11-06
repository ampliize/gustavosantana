# Press kit · Gustavo Santana

Site estático (um `index.html`) do press kit do Gustavo Santana, com o novo CD **Puro Sentimento** na capa e a discografia em CDs que giram, cada um com a capa do seu álbum no Sua Música.

## Editar
Tudo o que muda fica no bloco `EDITE AQUI` do `index.html`:
- `LINKS.whatsapp`: número com DDI e DDD (ex.: `5571999999999`). Preenchido, aparece um disco e um link de WhatsApp.
- `LINKS.fotos` / `LINKS.midiaKit`: links de pastas (Drive). Preenchidos, viram discos extras.
- `SM_TOTAIS` / `SM_DATA`: números do perfil no Sua Música.
- `MUSICA`: a faixa que toca no site (arquivo em `assets/`).
- `CDS`: os 6 CDs mais recentes, gerado por `scripts/build_cds.py` a partir dos dados do Sua Música.

As capas ficam em `assets/capas/`.
