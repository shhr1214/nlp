(ns ch2)

(def f "hightemp.txt")

;; 10
(defn count-line [path]
  (with-open [rdr (clojure.java.io/reader path)]
    (count (line-seq rdr))))

(println (count-line f))
