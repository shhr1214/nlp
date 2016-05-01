(ns ch2
  (:require [clojure.string :as cstr]))

(def f "hightemp.txt")

;; 10
(defn count-line [path]
  (with-open [rdr (clojure.java.io/reader path)]
    (count (line-seq rdr))))

(println (count-line f))

;; 11
(defn tab2space [path]
  (let [content (slurp path)]
    (cstr/replace content #"\t" " ")))

(println (tab2space f))
