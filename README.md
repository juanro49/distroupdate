[![](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/images/0)](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/links/0)[![](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/images/1)](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/links/1)[![](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/images/2)](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/links/2)[![](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/images/3)](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/links/3)[![](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/images/4)](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/links/4)[![](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/images/5)](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/links/5)[![](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/images/6)](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/links/6)[![](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/images/7)](https://sourcerer.io/fame/juanro49/juanro49/distroupdate/links/7)

# DistroUpdate
GNU/Linux Update Manager para distribuciones basadas en Debian o Ubuntu basado en Linux Mint Update Manager ([mintupdate](https://github.com/linuxmint/mintupdate))

<img src="https://i.imgur.com/ZlAOKKb.png"/>

## Instalación

### [PatoJAD Repo](https://patojad.com.ar/repositorio/)
- Añadir PatoJAD Repo al sistema
```
echo 'deb https://gitlab.com/patojad/repository/raw/patojad/debs/ patojad main' | sudo tee /etc/apt/sources.list.d/patojad.list
wget -qO - https://gitlab.com/LynxOS/repository/raw/lynxos/LynxPub.gpg | apt-key add -
sudo apt update
```
- Instalar paquete
```
sudo apt install distroupdate
```

### Paquete deb
```
wget https://github.com/juanro49/distroupdate/releases/download/5.6.1/distroupdate_5.6.1_all.deb
sudo dpkg -i distroupdate_5.6.1_all.deb
```

#### Menciones
- InstaTecno --> [DistroUpdate, herramienta gráfica para actualizar GNU/Linux fácilmente](https://instatecno.com/actualiza-gnu-linux-sin-comandos-distroupdate)
- PatoJAD --> [Actualiza GNU/Linux sin comandos con DistroUpdate](https://patojad.com.ar/aplicaciones/2020/04/actualiza-gnu/linux-sin-comandos-con-distroupdate/)

## Donaciones
| Método | Dirección |
| --- | --- |
| **Paypal** | https://www.paypal.me/juanro49 |
| **Bitcoin** | 1QJfiEAxa1A4TbEgtbVMHPXPWXJXxEpUvi |
| **Ethereum y tokens** | 0xb9d9958e73b44325082a2870830dca0d881490d2 |
| **Stellar** | GCOHJZYRBOQYIV265UDAB75VU3O2RFQ3TWHFPER32MSOKZCCKRKVBWEH |
| **Litecoin** | LYsyYEmxnRaCY3ML2tKYZpQA6zhndpuuQ4 |
| **Dash** | XxhbofmRrJSm5t4Lp9zSjECbe2v9LVdZcK |
| **MintUpdate** | https://www.linuxmint.com/donors.php |
| **PatoJAD repo** | https://patojad.com.ar/repositorio/ |
