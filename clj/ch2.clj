(ns ch2
  (:require [clojure.string :as cstr]))

(def f "hightemp.txt")

;; 10
(defn count-line [path]
  (with-open [rdr (clojure.java.io/reader path)]
    (count (line-seq rdr))))

;; (println (count-line f))

;; 11
(defn tab2space [path]
  (let [content (slurp path)]
    (cstr/replace content #"\t" " ")))

;; (println (tab2space f))

;; 12
(defn txt->seq [path]
  (with-open [rdr (clojure.java.io/reader path)]
    (let [lines (line-seq rdr)]
      (doall (seq lines)))))

(defn get-nth-from-line [lines n]
  (loop [lines lines
         result []]
    (if (empty? lines)
      result
      (recur (rest lines)
             (conj result (nth (cstr/split (first lines) #"\t") n))))))

(defn split-txt [path]
  (let [col1 (get-nth-from-line (txt->seq path) 0)
        col2 (get-nth-from-line (txt->seq path) 1)]
    (do
      (spit "col1.txt" (cstr/join "\n" col1))
      ;; (println (cstr/join #"\n" col1))
      (spit "col2.txt" (cstr/join "\n" col2)))))
      ;; (println (cstr/join #"\n" col2)))))

;; (split-txt f)

;; 13
(defn merge-txt [f1 f2]
  (loop [f1 (cstr/split (slurp f1) #"\n")
         f2 (cstr/split (slurp f2) #"\n")
         result ""]
    (if (or (empty? f1) (empty? f1))
      (spit "merge.txt" result)
      (recur (rest f1)
             (rest f2)
             (str result (first f1) "\t "(first f2) "\n")))))

(merge-txt "col1.txt" "col2.txt")
