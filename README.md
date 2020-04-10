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
