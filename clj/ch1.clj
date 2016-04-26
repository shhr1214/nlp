(ns ch1
  (:require [clojure.string :as s]))

;; 00
(defn reverse-string [s1]
  (s/reverse s1))

;; 01
(def patato "パタトクカシーー")

(defn extract-string [s1]
  (s/join (take-nth 2 s1)))

(println (extract-string patato))

;; 02
(def patrol-car "パトカー")
(def taxi "タクシー")

(defn join-string [s1 s2]
  (s/join (interleave s1 s2)))

(println (join-string patrol-car taxi))

;; 03
(def pi "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")

(defn get-capitals [s1]
  (s/join (map #(nth % 0) (s/split s1 #" "))))

(println (get-capitals pi))

;; 04
(def symbols "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
(def sym-nums #{1 5 6 7 8 9 15 16 19})

(defn get-string-from-symbols [symbols sym-nums]
  (loop [result ""
         lst (s/split symbols #" ")
         num 1]
    (if (nil? (first lst))
      result
      (recur (str result (if (contains? sym-nums num)
                           (subs (first lst) 0 1)
                           (subs (first lst) 0 2)))
             (rest lst)
             (+ num 1)))))

(println (get-string-from-symbols symbols sym-nums))
