# Git

## Synopsis

* git init
* git status
* git add
* git commit
* git remote
* git push
* git diff
* git pull
* git log

Weitere Kommandods: mkdir (Verzeichnis erstellen), touch (leere Datei anlegen)

## 01 Was ist Git und GitHub?

* https://github.com/

Andere Services verfügbar, an Universitäten oft GitLab, z.B. am URZ der
Universität Leipzig, https://git.sc.uni-leipzig.de/.

## 02 Anfang

```
$ mkdir hello-world
$ cd hello-world
```

Initialisierung.

```
$ git init
```


Status.

```
$ git status
```

Datei anlegen.

```
$ touch index.md
```

Datei für einen Commit vormerken.

```
$ git add index.md
```

Datei editieren, mit Editor der Wahl, z.B. [Visual Studio Code](https://code.visualstudio.com/) oder Notepad.

[...]

Einen Commit erstellen.

```
$ git commit -m "Add index.md"
```


## 03 Teilen / Sharing

Vorher: Ein Repository auf GitHub erstellen.


Verbinden des lokalen mit dem entfernten (remote) Repository.

```
$ git remote add origin https://github.com/some-librarian/hello-world.git
```


Anzeigen der entfernten Repositories.

```
$ git remote -v
```

Änderungen übertragen (pushen).

```
$ git push -u origin master
```

Änderungen anzeigen lassen.

```
$ git diff
```

Die versionsgeschichte anzeigen lassen.

```
$ git log
```

Weitere Änderungen übertragen.

```
$ git push
```

Änderungen beziehen.

```
$ git pull
```

## 04 Review

[...]

## 05 GitHub Pages

[...]


