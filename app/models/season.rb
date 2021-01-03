class Season < ApplicationRecord
    has_many :crops
    has_many :forages
    has_many :fish
end
